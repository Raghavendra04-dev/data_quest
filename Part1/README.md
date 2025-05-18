## Implementation
Actual lambda function code is part of the zip file **bls_data.zip**. This contains main logic along with dependecies like *requests, beautiful soup*. However, for easier review the main python file **fetch_bls_data.py** is also committed to same repo.
### Environment variables
- S3 Bucket: rearcdataquestbucket
- Directory: bls_data/
- Source url: https://download.bls.gov/pub/time.series/pr/

### Logic

1. The above mentioned parameters are used as environment variables to prevent hard coded values within the lambda function.
2. The code essentially checks for list of files available in the given S3 bucket and keeps them in a list.
3. Next, it gets the data from *source_url* and web-scraping is done using *beautifulsoup* for getting the required files.
4. The files from *source_url* are added, updated or deleted based on S3 bucket. This way if there are no changes on source side, S3 bucket will not be overwritten.
 



