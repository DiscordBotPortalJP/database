from fastapi import FastAPI
from pydantic import BaseModel


class Bot(BaseModel):
    name: str


app = FastAPI(
    title='Discord Bot Database',
    docs_url='/'
)


@app.get('/api/bots')
def get_bots():
    return {'message': 'Hello World'}


@app.get('/api/bots/{id}')
def get_bot(id: int):
    return {'message': 'Hello World'}


@app.post('/api/bots')
def post_bots(bot: Bot):
    return {'message': 'Hello World'}


@app.put('/api/bots/{id}')
def put_bots(id: int, bot: Bot):
    return {'message': 'Hello World'}


@app.delete('/api/bots/{id}')
def delete_bots(id: int):
    return {'message': 'Hello World'}
