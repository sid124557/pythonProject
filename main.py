from fastapi import FastAPI

app = FastAPI()


@app.get('/blog')
def index(sort: Optional [str], limit=10, published: bool = True  ):
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
def comments(id):
    return {'data': ('1', '2', '3')}
