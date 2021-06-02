from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # limited amount of blogs
    if published:
        return {'data': f'blog list {limit}'}
    else:
        return {'data': 'all the blogs'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id, limit = 10):
    return {'data': {'comment 1', 'comment 2', limit}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is cretaed with {request.title}'}
