# data_quest 
## Design

![Design drawio](https://github.com/user-attachments/assets/13851132-7a39-464a-b5f2-a96eec772dc7)

## Overview
The *data_quest* project is implemented using AWS cloud. The project can be broadly categorised into 2 parts:
1. Ingestion Layer
2. Processing Layer

### Ingestion Layer
This layer is responsible for bringing the data from different sources in to S3 bucket. Only 1 S3 bucket is used. However, the data is stored in separate directories. Implementation is done using AWS lambda functions. There are 2 lambda functions in this layer.
1. bls_data:
   - responsible for fetching the time series data from `bls.gov` website. The data files are stored in *s3://rearcdataquestbucket/bls_data/*
   - Source code: /Part1/fetch_bls_data.py
3. getUSApopulationdata:
   - responsible for fetching json data from `https://datausa.io/api/data`. The json file is stored in *s3://rearcdataquestbucket/population/*
   - Source code: /Part2/fetch_usa_population_data.py

Please refer to readme files under each part for more details.

### Processing Layer
This layer is responsible for performing all the required analysis. The input for this layer is the S3 bucket and processing is done using jupyter notebook. Since the data volume is less pandas are used for processing, otherwise we can use Spark.<br>
Source code: /Part3/data_analytics.ipynb
