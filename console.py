import pymongo
from pymongo import MongoClient

def getMoviesbyID(db, value ):
    collection = db.movies
    movieId='movieId'
    query= {movieId: value}
    projection={id:0}
    cursor = collection.find(query, projection)
    for record in cursor:
            print(record)
    menu(db)

def getMoviesbyTitle(db, value, limitValue ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
            print(record)
    menu(db)

def getMoviesbyGenre(db, value, limitValue ):
    collection = db.movies
    id="_id"
    genres="genres"
    query= {genres: value}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        print(record)
    menu(db)

def getMoviesbyYear(db, value, limitValue ):
    collection = db.movies
    id="_id"
    title="title"
    regex = '$regex'
    query= {title: { regex: value}}
    projection={id:0}
    cursor = collection.find(query, projection).limit(limitValue)
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

def getMoviesbyUserId(db, value , limitValue):
    collection = db.tags
    id="_id"
    userid="userId"
    movieId='movieId'
    title="title"
    movieIdList = []
    query= {userid: value}
    projection={id:0, movieId :1}
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
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    menu(db)

def getLowlyRatedMovies(db, limitValue ):
    collection = db.ratings
    rating='rating'
    lte='$lte'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating:{lte:0.5}}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    menu(db)

def getMoviebyRating(db, value, limitValue ):
    collection = db.ratings
    rating='rating'
    id="_id"
    movieId="movieId"
    title="title"
    movieIdList = []
    query= {rating: value}
    projection={movieId:1,id:0}
    cursor = collection.find(query, projection).limit(limitValue)
    for record in cursor:
        movieIdList.append(record['movieId'])
    ink = '$in'
    query = {movieId: { ink: movieIdList}}
    projection={id:0, title: 1}
    collection = db.movies
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    menu(db)

def print_menu():
    menu_option={
        1: 'Find Movies by ID', 
        2: 'Find Movies by Title',
        3: 'Find Movies by Genre.', 
        4: 'Find Movies by Year', 
        5:'Find Movies by User Id', 
        6: 'Insert a Movie', 
        7: 'Find Highly Rated Movies', 
        8: 'Find Lowly Rated Movies',
        9: 'Find Movies by Rating',
        10: 'Exit'
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
        limitValue = int(input('Enter limit: '))
        getMoviesbyTitle(db, value, limitValue)
    if option==3:
        value = int(input('Enter movie genre: '))
        limitValue = int(input('Enter limit: '))
        getMoviesbyGenre(db, value, limitValue)
    if option==4:
        value = str(input('Enter year: '))
        limitValue = int(input('Enter limit: '))
        getMoviesbyYear(db, value, limitValue)
    if option==5:
        value = int(input('Enter User ID: '))
        limitValue = int(input('Enter limit: '))
        getMoviesbyUserId(db, value, limitValue)
    if option==6:
        titleValue = str(input('Enter Movie title (Please use "Title (Year)"): '))
        genreValue = str(input('Enter Movie Genres (Please use "Genre1, Genre2"): '))
        addMovie(db, titleValue, genreValue)
    if option==7:
        limitValue = int(input('Enter limit: '))
        getHighlyRatedMovies(db, limitValue)
    if option==8:
        limitValue = int(input('Enter limit: '))
        getLowlyRatedMovies(db, limitValue)
    if option==9:
        value = int(input('Enter Rating: '))
        limitValue = int(input('Enter limit: '))
        getMoviebyRating(db, value, limitValue)
    if option==10:
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
