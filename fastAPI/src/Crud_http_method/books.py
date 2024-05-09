from fastapi import FastAPI

app = FastAPI()

Books = [{'title': 'title one', 'author': 'author one', 'category': 'science'},{'title': 'title two', 'author': 'author two', 'category': 'fiction'},{'title': 'title three', 'author': 'author three', 'category': 'thriller'},{'title': 'title four', 'author': 'author four', 'category': 'philosophy'},{'title': 'title five', 'author': 'author five', 'category': 'drama'}];

@app.get("/")
async def first_api():
    return {"message": "Hello from FastAPI! hit '/docs' end-point to see all of the routes"}

@app.get("/books")
async def books():
    return Books;
