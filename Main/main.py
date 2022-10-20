from fastapi import FastAPI

app = FastAPI()

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