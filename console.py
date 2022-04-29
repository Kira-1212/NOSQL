import pymongo
from pymongo import MongoClient

def getMoviesbyID(db, value ):
    collection = db.movies
    movieId='movieId'
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)
    menu(db)

def getMoviesbyTitle(db, value ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
            print(record)
    menu(db)

def getMoviesbyGenre(db, value ):
    collection = db.movies
    id="_id"
    genres="genres"
    query= {genres: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        print(record)
    menu(db)

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
    menu(db)

def addMovie(db, titleValue, genreValue ):
    collection = db.movies
    id="_id"
    title="title"
    movieId = "movieId"
    genres = 'genres'
    genreValue = genreValue.split(",")
    movieIdValue = 0
    
    cursor = collection.find(sort=[("movieId", pymongo.DESCENDING)]).limit(1)
    for record in cursor:
        movieIdValue = int(record["movieId"]) + 1
    
    insertValue ={
        movieId : movieIdValue,
        title : titleValue,
        genres : genreValue
    }
    insertRes = collection.insert_one(insertValue)
    print("Inserted this value", insertRes)
    query= {movieId: movieIdValue}
    projection={id:0}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    menu(db)

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
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        print(record)
    menu(db)

def getHighlyRatedMovies(db, limitValue ):
    collection = db.ratings
    rating='rating'
    gte='$gte'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating:{gte:5}}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        print(record)
    menu(db)

def print_menu():
    menu_option={
        1: 'Find Movie by ID', 
        2: 'Find Movie by Title',
        3: 'Find Movie by Genre.', 
        4: 'Find Movie by Year', 
        5:'Find Movie by User Id', 
        6: 'Insert a Movie', 
        7: 'Find Highly Rated Movies', 
        8: 'Exit'
        }
    for key, value in menu_option.items():
        print(key,".", value)


def menu(db):
    print_menu()
    option = int(input('Enter your choice: '))
    print(option)
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
    if option==7:
        limitValue = int(input('Enter limit: '))
        getHighlyRatedMovies(db, limitValue)
    if option==8:
        print("Exiting menu.....")



def main():
    try:
            conn = MongoClient("mongodb://127.0.0.1:27017")
            print("Mongo db Connected successfully!!!")
    except:
            print("Could not connect to MongoDB")
    
    db = conn.moviesDB
    menu(db)

if __name__ == "__main__":
    main()
