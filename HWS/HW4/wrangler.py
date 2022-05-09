# importing required libraries
import json
from numpy import record
import pandas as pd 

# creating a list to save each line in the json file
records= []

# iterating over the lines in the file
for line in open('zips.json', 'r'):
    # appending the json in each line to the list
    records.append(json.loads(line))
#converting the list of records to df
df = pd.DataFrame(records)
# saving the df to the csv
df.to_csv('zips-json.csv', index=False)