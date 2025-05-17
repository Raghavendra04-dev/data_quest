## Implementation
Actual lambda function code is part of the zip file **getUSApopulationdata.zip**. However, for easier review the main python file **fetch_usa_population_data.py** is also committed to same repo.

- S3 Bucket: rearcdataquestbucket
- Directory: population/
- Source url: https://datausa.io/api/data?drilldowns=Nation&measures=Population
- file_name: usa_population.json

### Logic

1. The above mentioned parameters are used as environment variable to prevent hard coded values within the lambda function.
2. The code get the data from the *source_url* and overwrites into <S3 bucket/population/>
   
