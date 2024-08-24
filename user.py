# Funções
# 1. Login com número da conta e PIN
# 2. Sair da conta
# 3. Visualização de dados cadastrais

# Estrutura de Dados
# 1. Nome do titular
# 2. PIN (Senha)

from fastapi import FastAPI

app = FastAPI()

@app.get("/B")
def B():
    return {"CHAMANDO B"}