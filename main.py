from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import mysql.connector
from Movie import Movie


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="movies_crud"
)

mycursor = mydb.cursor()

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI"}

#get all movies
@app.get("/movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies =  mycursor.fetchall()
    return movies

# get single movie by id
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    sql = "SELECT * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    movie =  mycursor.fetchall()
    if len(movie) == 0:
        raise HTTPException(status_code=500,detail='Movie not found!')
    return movie

# get single movie by title
@app.get("/movie_by_title/{movie_title}")
def get_movie_by_title(movie_title:str):
    sql = "SELECT * FROM movies WHERE title = %s"
    val = (movie_title,)
    mycursor.execute(sql,val)
    movie =  mycursor.fetchall()
    if len(movie) == 0:
        raise HTTPException(status_code=500,detail='Movie not found!')
    return movie

# #delete movie
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"message":"movie has been deleted successfully"}

# #create movie
@app.post("/movie")
def create_movie(movie:Movie):
    sql = "INSERT into movies (title,year) VALUES (%s,%s)"
    val = (movie.title,movie.year)
    mycursor.execute(sql,val)
    mydb.commit()
    return movie

# # update movie
@app.post("/update/movie")
def update_movie(movie_id:int,movie:Movie):
    sql = "UPDATE movies SET title=%s,year=%s WHERE id = %s"
    val = (movie.title,movie.year,movie_id)
    mycursor.execute(sql,val)
    mydb.commit()

    return movie
