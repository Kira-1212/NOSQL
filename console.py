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
    qstr = "/" + str(value) + "/"
    query= {title: qstr}
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
    qstr = "/" + str(value) + "/"
    print(qstr)
    query= {title: value}
    projection={id:0}
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




menu_option={1: 'Find Movie by ID', 2: 'Find Movie by Title',3: 'Find Movie by Genre.', 4: 'Find Movie by Year', 5:'Find Popular Businesses'}
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


