## Implementation
This layer is implemented using Jupyter notebook running locally. Data Processing is done using pandas as the volume of data is less. The same logic can also be implemented using Spark.
In the implementation Jupyter notebook extension is installed on VS code, but in actual use case it can be deployed on an EC2 instance or downloaded from AWS marketplace.
There are 2 main files in this implementation:
1. **`variable.env`**: contains all the parameters to prevent hard-coding
2. **`data_analytics.ipynb`**: main logic 

### Logic
The logic is based on the requirement mentioned in the **Part 3: Data Analytics** section of https://github.com/rearc-data/quest
1. Load both the csv file from Part 1 pr.data.0.Current and the json file from Part 2 as dataframes (Spark, Pyspark, Pandas, Koalas, etc).
2. Using the dataframe from the population data API (Part 2), generate the mean and the standard deviation of the annual US population across the years [2013, 2018] inclusive.
3. Using the dataframe from the time-series (Part 1), For every series_id, find the best year: the year with the max/largest sum of "value" for all quarters in that year. Generate a report with each series id, the best year for that series, and the summed value for that year.
4. Using both dataframes from Part 1 and Part 2, generate a report that will provide the value for series_id = PRS30006032 and period = Q01 and the population for that given year (if available in the population dataset). 
