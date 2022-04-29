import pymongo


def getMoviesbyID(db, value ):
    collection = db.movies
    movieId='movieId'
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)
def getMoviesbyTitle(db, value ):
    collection = db.movies
    id="_id"
    title="title"
    #qstr = "/" + str(value) + "/"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)

def getMoviesbyGenre(db, value ):
    collection = db.movies
    id="_id"
    genres="genres"
    query= {genres: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)

def getMoviesbyYear(db, value ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)

def addMovie(db, titleValue, genreValue ):
    collection = db.movies
    id="_id"
    title="title"
    movieId = "movieId"
    genres = 'genres'
    genreValue = genreValue.split(",")
    movieIdValue = 0
    print(genreValue)
    
    cursor = collection.find().sort({"movieId" : pymongo.DESCENDING}).limit(1)
    for record in cursor:
        movieIdValue = int(record["movieId"]) + 1
    insertValue ={
        movieId : movieIdValue,
        title : titleValue,
        genres : genreValue
    }
    print(insertValue)

def getMoviesbyUserId(db, value ):
    collection = db.tags
    id="_id"
    userid="userId"
    movieId='movieId'
    title="title"
    movieIdList = []
    query= {userid: value}
    projection={id:0, movieId :1}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        #record.split(":")
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        print(record)

def fetch_popular_business(db):
    collection = db.yelpc
    is_open="is_open"
    id="_id"
    name="name"
    review_count="review_count"
    query={is_open:1}
    projection={name:1,id:0, review_count:1}
    sort_query= {review_count:-1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)




menu_option={1: 'Find Movie by ID', 2: 'Find Movie by Title',3: 'Find Movie by Genre.', 4: 'Find Movie by Year', 5:'Find Movie by User Id', 6: 'Insert a Movie'}
def print_menu(menu_option):
    for key, value in menu_option.items():
        print(key,".", value)
print_menu(menu_option)
option = int(input('Enter your choice: '))
print(option)

from pymongo import MongoClient

try:
        conn = MongoClient("mongodb://127.0.0.1:27017")
        print("Connected successfully!!!")
except:
        print("Could not connect to MongoDB")
db = conn.moviesDB
if option==1:
    value = int(input('Enter movie id: '))

    getMoviesbyID(db, value)
if option==2:
    value = str(input('Enter movie title: '))
    getMoviesbyTitle(db, value)


if option==3:
    value = int(input('Enter movie genre: '))
    getMoviesbyGenre(db, value)

if option==4:
    value = str(input('Enter year: '))
    getMoviesbyYear(db, value)

if option==5:
    value = int(input('Enter User ID: '))
    getMoviesbyUserId(db, value)
if option==6:
    titleValue = str(input('Enter Movie title (Please use "Title (Year)"): '))
    genreValue = str(input('Enter Movie Genres (Please use "Genre1, Genre2"): '))
    addMovie(db, titleValue, genreValue)
