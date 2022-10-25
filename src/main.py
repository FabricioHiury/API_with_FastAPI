from turtle import position
from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional 
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins = ["http://localhost:5500/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/profile")
async def profile():
    return{"name": "Fabrício Hiury"}

@app.post("/profile")
async def signup():
    return{"mensagem": "Perfil criado com sucesso!"}

@app.put("/profile")
async def update():
    return{"mensagem": "Perfil atualizado com sucesso!"}

@app.delete("/profile")
async def remove():
    return{"mensagem": "Perfil removido!"}

@app.get("/saudacao/{name}")
async def saudacao(name: str):
    text = f'Olá {name}, é um prazer vê-lo novamente!'
    return text 

class Products(BaseModel):
    id: Optional[str]
    name: str
    price: float

@app.post("/products")
async def products(product: Products):
    return {"mensagem": f"O produto {product.name} de valor R${product.price} foi cadastrado com sucesso!"}

bank: List[Products] = []

@app.get("/products")
def list_products():
    return bank

@app.get("/products/{product_id}")
def get_products(product_id: str):
    for product in bank:
        if product.id == product_id:
            return product
    return {'error': 'Product not found'} 

@app.delete("/products/{product_id}")
def delete_products(product_id: str):
    position = -1
    for index, product in enumerate(bank):
        if product.id == product_id:
            position = index
            break
    if position  != -1:
        bank.pop(position)
        return{'mensagem': 'Product deleted'}
    else:
        return {'mensagem' : f'Product not found with id {id}'}

@app.post("/products")
def create_products(product: Products):
    product.id = str(uuid4())
    bank.append(product)
    return None