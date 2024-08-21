from typing import Union
from fastapi import FastAPI

import banking

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/teste")
def teste():
    return ("Teste Texto para o gustavo")
  
@app.post("/teste2")
def testando():
    return banking.teste2()