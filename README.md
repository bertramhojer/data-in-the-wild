## ⚡ Investigating the Relationship between Employee Reviews and Financial Performance: A Study Using [Glassdoor](www.glassdoor.com) Reviews and Stock Prices ⚡
### ✨ Data in the Wild: Wrangling and Visualising Data (Autumn 2022) ✨

**Abstract**
This paper presents a dataset containing employee reviews and company stock prices from Glassdoor.com and Yahoo Finance. The motivation for creating this dataset is to investigate the relationship between employee perception of a company, as reflected in glassdoor.com reviews, and its financial performance, as reflected in stock prices, for large public technology companies in the U.S. The paper poses three research questions: (1) how well do review text and ratings align on glassdoor.com, (2) is there a relationship between employee perception of a company and its stock price, and (3) which topics and tendencies are prevalent in employee reviews and how have they evolved over time? The paper investigates these questions using sentiment analysis, annotation, cross-correlation analysis on time-series data, and statistical hypothesis testing. The findings suggest that review text and ratings have a fair alignment, but that there is no strong correlation between ratings and stock price for the companies studied. The paper concludes by discussing the potential applications of the dataset and suggesting future research directions.

We have employed clustering methods as well as time-series correlation analyses to assess potential trends. Additionally we do some statistical analyses of different groups of reviewers to showcase the usability of the dataset.

## 📖 Documentation

`configs.json` is the configurations file for `data_processing.ipynb`. The analysis can be adjusted by changing this config.

`raw_data/` holds the raw data scraped using the configurations as they are provided in the configs.json.

`review_scraper.py` is the script doing the scraping.

`data_processing.ipynb` reads and processes the raw data files in `raw_data` to output the final dataset.

`timeseries_analysis.ipynb` contains the time series analysis along with the plots used in the report.

`topic_over_time.ipynb` is the topic modelling analysis.

`visualization.ipynb` is the notebook to generate the chart included in the report.

`review_data.csv` is the final data set.

`irr_analysis.ipynb` is the notebook that calculates the inter-rater reliability agreement

`sampling_annotation.ipynb` strafity the samples and format it to fit [doccano] (https://github.com/doccano/doccano)

## 💻 Setup
`pip install -r requirements.txt`
