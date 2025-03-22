from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

#Logics:
Books = [{'title': 'title one', 'author': 'author one', 'category': 'science'},{'title': 'title two', 'author': 'author two', 'category': 'fiction'},{'title': 'title three', 'author': 'author three', 'category': 'thriller'},{'title': 'title four', 'author': 'author four', 'category': 'philosophy'},{'title': 'title five', 'author': 'author five', 'category': 'drama'}];

class Book:
    id: int = Field(gt=3, lt=7) #greater than, less than
    name: str = Field(min_length=3, max_length=7)
    
    def __init__(self, id, name):
        self.id = id,
        self.name = name

class BookValidator(BaseModel):
    id: int
    name: str

classBook = [
    Book(1,"book1"),
    Book(2,'book2')
]

obj = [
    {"name": "kire"},
    {"name": "oi"},
    {"id": 1}
]


#routes:
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
    #return [obj,classBook] #passing them in a list where both have separate list inside a new list
    return obj+classBook #concatenating them into one array instead of separated list.

#post req
@app.post("/create-book")
async def create_book(book_req= Body()):
    Books.append(book_req)

@app.post("/add-book")
async def validated_book(books_req= BookValidator):
    #convert the req data to Book obj/dictionary and ** allows to assign those key-val of the obj/dictionary into keyword arguments that needed to the Book constructor.i.e: key of id, name of the req dictionary/object will be assigned to the id and name of the constructor of the Book class. meaning, ** and .model_dump() converts req to Obj/dict and passed the keys of it to that obj/dict. so, flow is: convert req to dict -> take keys of the dicts and assign them to the Book constructor.
    new_book=Book(**books_req.model_dump())
    Books.append(new_book)