## ⚡ Investigating the Relationship between Employee Reviews and Financial Performance: A Study Using Glassdoor Reviews and Stock Prices ⚡
### Data in the Wild: Wrangling and Visualising Data (Autumn 2022)

**Abstract**
This paper presents a dataset containing employee reviews and company stock prices from Glassdoor.com and Yahoo Finance. The motivation for creating this dataset is to investigate the relationship between employee perception of a company, as reflected in glassdoor.com reviews, and its financial performance, as reflected in stock prices, for large public technology companies in the U.S. The paper poses three research questions: (1) how well do review text and ratings align on glassdoor.com [www.glassdoor.com], (2) is there a relationship between employee perception of a company and its stock price, and (3) which topics and tendencies are prevalent in employee reviews and how have they evolved over time? The paper investigates these questions using sentiment analysis, annotation, cross-correlation analysis on time-series data, and statistical hypothesis testing. The findings suggest that review text and ratings have a fair alignment, but that there is no strong correlation between ratings and stock price for the companies studied. The paper concludes by discussing the potential applications of the dataset and suggesting future research directions.

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
