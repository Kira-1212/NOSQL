import pandas
li =[]
df = pandas.read_csv("zips-json.csv", header=0)
for index, row in df.iterrows():
    li.append(row['loc'].split(','))
df = df.drop('loc', 1)
df['loc'] = li
df.to_csv('zips.csv')