## Data in the Wild: Wrangling and Visualising Data (Autumn 2022)

**Introduction**

It is in the interest of any public company to increase
their stock-price to keep investors happy and to maintain a good brand. This project presents the creation of a new dataset that explores the relationship between glassdoor reviews and stock market price. The dataset was created by collecting glassdoor reviews for a sample of publicly traded companies and pairing them with stock market price data for the same period. The dataset provides a rich source of information for researchers interested in studying the impact of employee sentiment on stock market performance. The paper also provides a detailed description of the data collection and cleaning processes, as well as some preliminary analysis of the dataset. We attempt to model a relationship between stock-prices of large public technology companies and employee reviews on [glassdoor](https://www.glassdoor.com/). We hypothesise that employee-reviews and stock-price may be correlated with a time-lag. We do not conclude anything with
their stock-price to keep investors happy and to maintain a good brand. This project presents the creation of a new dataset that explores the relationship between glassdoor reviews and stock market price. The dataset was created by collecting glassdoor reviews for a sample of publicly traded companies and pairing them with stock market price data for the same period. The dataset provides a rich source of information for researchers interested in studying the impact of employee sentiment on stock market performance. The paper also provides a detailed description of the data collection and cleaning processes, as well as some preliminary analysis of the dataset. We attempt to model a relationship between stock-prices of large public technology companies and employee reviews on [glassdoor](https://www.glassdoor.com/). We hypothesise that employee-reviews and stock-price may be correlated with a time-lag. We do not conclude anything with
their stock-price to keep investors happy and to maintain a good brand. This project presents the creation of a new dataset that explores the relationship between glassdoor reviews and stock market price. The dataset was created by collecting glassdoor reviews for a sample of publicly traded companies and pairing them with stock market price data for the same period. The dataset provides a rich source of information for researchers interested in studying the impact of employee sentiment on stock market performance. The paper also provides a detailed description of the data collection and cleaning processes, as well as some preliminary analysis of the dataset. We attempt to model a relationship between stock-prices of large public technology companies and employee reviews on [glassdoor](https://www.glassdoor.com/).

We have employed clustering methods as well as time-series correlation analyses to assess potential trends. Additionally we do some statistical analyses of different groups of reviewers to showcase the usability of the dataset.

**Data Sources**

- Building a Selenium-based scraper to scrape company information from Glassdoor. This won’t be a crawler as we only want to investigate major companies. We need to use Selenium as Glassdoor uses a lot of Javascript.
    - Company, Title, Date, Review-text, Review-rating, Salary, Demographics
- Stock-prices related to major companies scraped from Glassdoor. We could e.g. use the [API of Yahoo Finance](https://rapidapi.com/apidojo/api/yh-finance) ⚡️
- Potentially combining key-events retrieved from major news-outlets at events from review data.

**Methodology**

- **Sentiment analysis** on employee reviews. We would then model the distribution of the sentiment of reviews for individual companies and compare these with the distribution of actual ratings within as well as between companies.
- **Clustering**; what are the main themes prevalent in reviews?
- **Temporal modelling** of employee satisfaction (sentiment and rating) combined with “key”-events and stock-prices (event-detection)? Company rating could be modelled temporally as a rolling average of ratings. This is what we’d then combine with e.g. stock prices. One might expect that we’d see general employee ratings of a company would fall as stock-prices go down. This would mainly be seen over longer time periods - as reviews are likely lagged in time.

**Challenges**

- Sparsity of data
- Who are the users on Glassdoor? Review sites generally encounter the issue of a small subset of “loud” people actually reviewing.
- The temporal dimension is most likely quite lagged.
- Review bias (what some see as a benefit, might be seen negatively by others)
- Data quality assurance
