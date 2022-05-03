import pandas as pd
import json
df = pd.read_csv('movies.csv')

li =[]
for index, row in df.iterrows():

    insertValue ={
            "movieId" : row['movieId'],
            "title" : row['title'],
            "genres" : row['genres']
        }
    li.append(insertValue)



final = json.dumps(li, indent=2)
  
# display
with open("movies.json", "w") as final:
   json.dump(li, final, indent=2)

print("movies done")

df = pd.read_csv('tags.csv')

li =[]
for index, row in df.iterrows():

    insertValue ={
            "userId" : row['userId'],
            "movieId" : row['movieId'],
            "tag" : row['tag'],
            "timestamp": row['timestamp']
        }
    li.append(insertValue)

# display
with open("tags.json", "w") as final:
   json.dump(li, final, indent=2)

print("tags done")


df = pd.read_csv('ratings.csv')

li =[]
for index, row in df.iterrows():

    insertValue ={
            "userId" : row['userId'],
            "movieId" : row['movieId'],
            "rating" : row['rating'],
            "timestamp": row['timestamp']
        }
    li.append(insertValue)

# display
with open("ratings.json", "w") as final:
   json.dump(li, final, indent=2)

print("ratings done")