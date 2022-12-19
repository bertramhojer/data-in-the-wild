from bs4 import BeautifulSoup
import time
import pandas as pd
import json
import os
import sys

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv(".env")
username = os.getenv("GLASSDOOR_USERNAME")
password = os.getenv("GLASSDOOR_PASSWORD")


def load_config():

    conf = open("config.json", "r")
    config = json.load(conf)
    sites = config["sites"]
    categories = config["categories"]
    conf.close()

    return sites, categories


def accept_cookies():
    try:
        driver.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        pass


# Return a driver that has been logged into the .env account
def login(username: str, password: str):  # -> tuple[driver, DataFrame]
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # install the driver when you login, way easier than setting up outside of the code
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get(
        "https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK"
    )

    # Click on e-mail field and hit enter
    time.sleep(0.5)
    driver.find_element("xpath", '//*[@id="inlineUserEmail"]').send_keys(username)
    time.sleep(0.1)
    driver.find_element("xpath", '//*[@class="css-2etp8b evpplnh1"]').click()
    # Click on password field and hit enter
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="inlineUserPassword"]').send_keys(password)
    time.sleep(0.1)
    driver.find_element("xpath", '//*[@class="css-2etp8b evpplnh1"]').click()
    time.sleep(1)

    # Accept cookies if they pop up
    accept_cookies()

    return driver


# expand a page and return the page-source
def expand_page(driver, url):
    driver.get(url)
    time.sleep(0.5)
    # Accept cookies if the pop up
    accept_cookies()
    # Find all 'Contine Reading' buttons and click them
    try:
        elements = driver.find_elements(
            "xpath", "//*[contains(@class, 'v2__EIReviewDetailsV2__continueReading')]"
        )
        for elem in elements:
            driver.execute_script("arguments[0].click();", elem)
    except:
        pass

    return driver.page_source


def extract_info(review):
    rating = review.find("span", class_="ratingNumber mr-xsm").text
    date_job = review.find(
        "span", class_="middle common__EiReviewDetailsStyle__newGrey"
    ).text.split("-")
    date, job_title = date_job[0], "".join(date_job[1:])
    review_title = review.find("a", class_="reviewLink").text
    pros = review.find("span", attrs={"data-test": "pros"}).text
    cons = review.find("span", attrs={"data-test": "cons"}).text
    try:
        employee_status, experience = review.find(
            "span", class_="pt-xsm pt-md-0 css-1qxtz39 eg4psks0"
        ).text.split(",")
    except:
        employee_status = review.find(
            "span", class_="pt-xsm pt-md-0 css-1qxtz39 eg4psks0"
        ).text
        experience = None
    try:
        author_location = review.find_all("span", class_="middle", limit=2)[1].text
    except:
        author_location = None
    try:
        advice = review.find("span", attrs={"data-test": "advice-management"}).text
    except:
        advice = None
    try:
        helpful = review.find(
            "div", class_="common__EiReviewDetailsStyle__socialHelpfulcontainer pt-std"
        ).text
    except:
        helpful = None

    return [
        rating,
        employee_status,
        date,
        job_title,
        review_title,
        pros,
        cons,
        experience,
        author_location,
        advice,
        helpful,
    ]


def scrape_page(driver, company, category, page):

    start = time.time()
    COMPANY_ID, JOB_ID = sites[company], categories[category]
    site = f"https://glassdoor.com/Reviews/Reviews-EI_IE{COMPANY_ID}.0,5_DEPT{JOB_ID}_IP{page}.htm?filter.iso3Language=eng"
    response = expand_page(driver, site)
    soup = BeautifulSoup(response, "html.parser")
    reviews = soup.find_all("div", class_="gdReview")
    assert len(reviews) > 0, "Error - No reviews found"

    columns = [
        "rating",
        "status",
        "date",
        "job_title",
        "review_title",
        "pros",
        "cons",
        "experience",
        "location",
        "advice",
        "helpful",
    ]
    review_data = [extract_info(review) for review in reviews]
    data = pd.DataFrame(columns=columns)

    for review in review_data:
        data.loc[len(data)] = review

    data["company"] = company
    data["category"] = category

    print(site, " -- Timer: ", round(time.time() - start, 2))

    return data


def write_data(site, category, data):

    data.columns = data.columns.astype(str)
    file = f"Reviews-{site}-{category}.parquet"
    previous_data = pd.read_parquet(f"Data/{file}").reset_index(drop=True)
    merged_data = pd.concat([previous_data, data]).reset_index(drop=True)
    merged_data.to_parquet(f"Data/{file}")


def run_scraper():

    for site in sites:
        for category in categories:
            page = 1
            data = pd.DataFrame(
                columns=[
                    "rating",
                    "status",
                    "date",
                    "job_title",
                    "review_title",
                    "pros",
                    "cons",
                    "experience",
                    "location",
                    "advice",
                    "helpful",
                    "company",
                    "category",
                ]
            )

            while True:
                try:

                    reviews = scrape_page(driver, site, category, page)
                    data = pd.concat([data, reviews])
                    time.sleep(0.1)
                    page += 1

                except Exception as e:

                    if str(e) == "Error - No reviews found":
                        print(e)
                        write_data(site, category, data)
                        break
                    else:
                        print(e)
                        break

                # Write the initial data file if we're on the first iteration of the loop
                if page == 2:
                    data.columns = data.columns.astype(str)
                    data.to_parquet(f"Data/Reviews-{site}-{category}.parquet")
                    data = pd.DataFrame(
                        columns=[
                            "rating",
                            "status",
                            "date",
                            "job_title",
                            "review_title",
                            "pros",
                            "cons",
                            "experience",
                            "location",
                            "advice",
                            "helpful",
                            "company",
                            "category",
                        ]
                    )

                # Write data from the latest 10 pages to the data-file
                elif page % 10 == 0:
                    write_data(site, category, data)
                    data = pd.DataFrame(
                        columns=[
                            "rating",
                            "status",
                            "date",
                            "job_title",
                            "review_title",
                            "pros",
                            "cons",
                            "experience",
                            "location",
                            "advice",
                            "helpful",
                            "company",
                            "category",
                        ]
                    )


if __name__ == "__main__":

    driver = login(username, password)
    time.sleep(1)
    sites, categories = load_config()
    total_start = time.time()

    run_scraper()

    print("total time: ", time.time() - total_start)
