from fastapi import Body, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

#Logics:
Books = [{'id':1,'title': 'title one', 'author': 'author one', 'category': 'science'},{'id':2,'title': 'title two', 'author': 'author two', 'category': 'fiction'},{'id':3,'title': 'title three', 'author': 'author three', 'category': 'thriller'},{'id':4,'title': 'title four', 'author': 'author four', 'category': 'philosophy'},{'id':5,'title': 'title five', 'author': 'author five', 'category': 'drama'}];

class Book:
    id: int
    name: str
    rating: int
    
    #if we use BaseModel then we don't need to initialize as baseModel does it for us.
    def __init__(self, id, name, rating=0):
        self.id = id,
        self.name = name
        self.rating = rating

class BookValidator(BaseModel):
    id: int = Field(gt=0, lt=7) #greater than, less than
    name: str = Field(min_length=3, max_length=7)
    rating: int = Field(gt=0, lt=7)
    
    class Config:
        # schema_extra (pydantic v1) is used to add extra fields to the schema. this is used to show example of the schema in the docs
        json_schema_extra = {
            'example': {
                "id": 4,
                "name": "book1",
                "rating": 4
            }
        }

classBook = [
    BookValidator(id=4, name="book1", rating=4),
    BookValidator(id=5, name="book2", rating=3)
]

obj = [
    {"name": "kire"},
    {"name": "oi"},
    {"id": 1}
]


#routes:
@app.get("/", status_code=status.HTTP_200_OK)
async def first_api():
    return {"message": "Hello from FastAPI! hit '/docs' end-point to see all of the routes"}

@app.get("/books", status_code=status.HTTP_200_OK)
async def books():
    return Books;

@app.get("/rating/", status_code=status.HTTP_200_OK)
async def find_book_by_rating(rating: int = Query(gt=0,lt=7)):
    books_to_return = []
    for book in classBook:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return

#returning list consist of two types of obj, created by class and object notation.
@app.get("/class", status_code=status.HTTP_200_OK)
async def classBook1():
    #return [obj,classBook] #passing them in a list where both have separate list inside a new list
    return obj+[book.model_dump() for book in classBook] #concatenating them into one array instead of separated list. Convert objects to dicts before concatenation

#post req
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_req= Body()):
    Books.append(book_req)
    return {"message": "Book added successfully"}

"""convert the req data to Book obj/dictionary and ** allows to assign those key-val of the obj/dictionary into keyword arguments that needed to the Book constructor.i.e: key of id, name of the req dictionary/object will be assigned to the id and name of the constructor of the Book class. meaning, ** and .model_dump() converts req to Obj/dict and passed the keys of it to that obj/dict. so, flow is: convert req to dict -> take keys of the dicts and assign them to the Book constructor."""
@app.post("/add-book", status_code=status.HTTP_201_CREATED)
async def validated_book(books_req: BookValidator):
    print(type(books_req))
    new_book=Book(**books_req.model_dump())
    # Books is storing Book obj and not dict here.
    Books.append(new_book)
    return {"message": "Book added successfully"}

@app.put("/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_req: BookValidator):
    book_changed = False
    for i in range(len(classBook)):
        if classBook[i].id == book_req.id:
            Books[i]=book_req
            book_changed = True
            return {"message": "Book updated successfully"}
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

# without defining path parameter delete would work as well in the form of query parameter.
@app.delete("/delete-book/{book_id}", status_code=status.HTTP_204_NO_CONTENT) #book_id is the path parameter
async def delete_book(book_id: int):
    book_deleted = False
    for i in range(len(Books)):
        if Books[i]["id"] == book_id:
            Books.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

#find specific book
@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def find_book_by_id(id:int = Path(gt=0,lt=7)):
    for book in Books:
        if book["id"] == id:
            return book
    # Raise an exception if the book is not found
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/book-obj/{id}", status_code=status.HTTP_200_OK)
async def find_book_by_id(id: int = Path(gt=0,lt=7)):
    for book in classBook:
        if book.id == id:
            return book
    # Raise an exception if the book is not found
    raise HTTPException(status_code=404, detail="Book not found")