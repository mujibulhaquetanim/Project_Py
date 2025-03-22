from fastapi import FastAPI

app = FastAPI()

Books = [{'title': 'title one', 'author': 'author one', 'category': 'science'},{'title': 'title two', 'author': 'author two', 'category': 'fiction'},{'title': 'title three', 'author': 'author three', 'category': 'thriller'},{'title': 'title four', 'author': 'author four', 'category': 'philosophy'},{'title': 'title five', 'author': 'author five', 'category': 'drama'}];

class Book:
    id: int
    name: str
    
    def __init__(self, id, name):
        self.id = id,
        self.name = name

classBook = [
    Book(1,"book1"),
    Book(2,'book2')
]

obj = [
    {"name": "kire"},
    {"name": "oi"}
]

@app.get("/")
async def first_api():
    return {"message": "Hello from FastAPI! hit '/docs' end-point to see all of the routes"}

@app.get("/books")
async def books():
    return Books;

@app.get("/wow")
async def wow():
    return "oi kire oi kire"

#returning list consist of two types of obj, created by class and object notation.
@app.get("/class")
async def classBook1():
    return [obj,classBook];
