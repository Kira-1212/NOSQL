# importing pandas
import pandas
# list to store the split values of loc
li =[]
# fetching the csv and storing it in dataframe
df = pandas.read_csv("zips-json.csv", header=0)
#iterating over the df rows
for index, row in df.iterrows():
    # foreach row splitting the value of the loc at , and appending it to list
    li.append(row['loc'].split(','))
# dropping previous loc column
df = df.drop('loc', 1)
# adding the new list to the df
df['loc'] = li
# storing the resulting df in csv
df.to_csv('zips.csv')