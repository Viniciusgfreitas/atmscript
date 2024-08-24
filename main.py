from typing import Union
from fastapi import FastAPI

import banking
import user

app = FastAPI()


# ----- Autenticação -----
# 1. Verificar o número da conta e o PIN para conceder acesso.

# ----- Consultas e Operações ------
# 1. Após o login, o usuário deve ter acesso ao menu principal com opções de operações.

# ----- Validação ------
# 1. Verificar se há saldo suficiente antes de realizar saques ou transferências.
# 2. Limitar o valor de saque por operação e por dia.

# ------ Registro de Transações ------
# 1. Cada operação deve ser registrada com os detalhes necessários para histórico.


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/teste")
def teste():
    return ("Teste Texto")
  
@app.post("/teste2")
def teste2():
    return banking.teste2()

@app.get("/userTeste")
def userTeste():
    return user.userTeste()