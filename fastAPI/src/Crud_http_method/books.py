from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

#Logics:
Books = [{'id':1,'title': 'title one', 'author': 'author one', 'category': 'science'},{'id':2,'title': 'title two', 'author': 'author two', 'category': 'fiction'},{'id':3,'title': 'title three', 'author': 'author three', 'category': 'thriller'},{'id':4,'title': 'title four', 'author': 'author four', 'category': 'philosophy'},{'id':5,'title': 'title five', 'author': 'author five', 'category': 'drama'}];

class Book:
    id: int
    name: str
    
    #if we use BaseModel then we don't need to initialize as baseModel does it for us.
    def __init__(self, id, name):
        self.id = id,
        self.name = name

class BookValidator(BaseModel):
    id: int = Field(gt=3, lt=7) #greater than, less than
    name: str = Field(min_length=3, max_length=7)

classBook = [
    BookValidator(id=4, name="book1"),
    BookValidator(id=5, name="book2")
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
    
#find specific book
@app.get("/books/{id}")
async def find_book_by_id(id:int):
    for book in Books:
        if book["id"] == id:
            return book
@app.get("/book-obj/{id}")
async def find_book_by_id(id: int):
    for book in classBook:
        if book.id == id:
            return book
    # Raise an exception if the book is not found
    raise HTTPException(status_code=404, detail="Book not found")