## Stock Prices Prediction Using Machine and Deep Learning Techniques

Traditionally, prediction of stock market performance done via technical analysis is extremely 
challenging, to say the least.  A varied spectrum of factors affect the prediction of stock price e.g. 
physical and psychological factors, rational and irrational behaviour, local and global events etc. 
These factors make share prices volatile and very difficult to reliably predict with a high degree of 
accuracy. 

This project aims to explore using machine and deep learning techniques, to complement traditional 
technical analysis, to be the game changer in stock price prediction.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSfH12Ky4XeihdhuOhTtYnTMFmOYcZ884lcXwWASPIuOavc642MMD_ZwzoEK6ivYyT0FRWci3vQrHD9/embed?start=true&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="false" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Database Design

The database design allows for the efficient storage and manipulation of price and features data.

####prices - Stock prices
1. id - Id of price row 
2. ticker - Ticker of company
3. interval - Interval of the price row i.e. daily (D), weekly (W), 1 minute (1), 5 minute (5)
4. datetime - Timestamp of price row
5. open - Opening price of interval
6. high - Highest price of interval
7. low - Lowest price of interval
8. close - Closing price of interval
9. volume - Number of shares traded in the interval

####features_dates - Date related features
1. id - Id of date feature row 
2. price_id - Foreign key to prices tables, id of related price row
3. year - Year of price datetime
4. month - Month of price datetime
5. day - Day of price datetime
6. hour - Hour of day of price datetime
7. minute - Minute of price datetime
8. wk_of_yr - Week of year of price datetime
9. day_of_yr - Day of year of price datetime
10. day_of_wk - Day of week of price datetime 
11. start_of_yr - Is start of the year?
12. end_of_yr - Is end of the year?
13. start_of_qtr - Is start of the quarter?
14. end_of_qtr Is end of the quarter?
15. start_of_mth - Is start of the month?
16. end_of_mth - Is end of the month?
17. start_of_wk - Is start of the week?
18. end_of_wk - Is end of the week?

####features_indicators - Technical indicators related features
1. id - Id of indicator feature row
2. price_id - Foreign key to prices tables, id of related price row
3. name - Name of indicator
4. parameters - Parameter to be supplied to indicator
5. value - Numeric value of the indicator, or 1 or 0 for binary e.g. oversold/bought condition

####symbols - Ticker to company name mappings
1. id - - Id of symbol row
2. ticker - Ticker of stock used in exchange/market
3. name - Name of company

###Web API

This package can be deployed as a cloud function on GCP to expose data retrieval functions to the 
Cloud SQL.  The web API entry point, as determined by GCP specifications, is the main.py script. 
This package has been uploaded to GCP's Source Repositories for ease of use within GCP.


####Python Package Index

This package has been uploaded to the Python Package Index under the title 'ga-capstone-hakngrow'.
Being on the index, you can install this package using pip. Files particularly important for uploading 
to the Index include setup.py, MANIFEST.in, LICENSE, README.md and requirements.txt. For further
details, refer to [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/).

###utils Package

- Config.py - Stores configuationr data used by this package
- AlphaVantageUtils.py - Interfaces with the AlphaVantage web API to retrieve stock prices 
- PostgresUtils.py - Database functions that interfaces with the GCP Cloud SQL database
- ModelUtils.py - Contains utility functions for use in ML and DL models
- PriceUpdater.py - Utility to update stock prices stored in Cloud SQL
- FeaturesUpdater.py - Utility to update stock price features stored in Cloud SQL  
 
###models Package

Contains various scripts using different models to perform price prediction.

###strategy Package

Contains scripts to perform strategy testing and back-testing.

###jupyter Folder

Contains Jupyter notebooks for purpose of model engineering and testing.
