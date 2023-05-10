#importa biblioteca API
from fastapi import FastAPI

#cria API
app = FastAPI()

vendas = {
    1: {"item": "lata", "preco-unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco-unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco-unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco-unitario": 2, "quantidade": 5},
}

#define a rota inicial, atribui funcionalidade de execao
@app.get("/")
def home():
    return {"Vendas": len(vendas)}



@app.get("/vendas/{id_vendas}")
def get_venda(id_venda: int): #faz a validacao se é um inteiro
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Error": "ID venda inexistente"}
