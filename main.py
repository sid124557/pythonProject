from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published == True:
        return {"data": f" {limit} published blog from db"}
    else:
        return {"data": f" {limit} blog from db"}


@app.get("/blog/unpublished")
def unpublished_blog():
    return {'data': 'all unpublished blog'}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": {id}}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': ('1', '2', '3')}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def blog_creat(request: Blog):
    return {'data': f'blog created as {request.title}'}
