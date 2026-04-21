from fastapi import FastAPI
import models
from database import engine

# Esse comando olha para o arquivo models.py e cria as tabelas no Supabase!
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API - GigaRoça & Café",
    description="Sistema de Gestão, Estoque e PDV para produtos mineiros",
    version="1.0.0"
)

@app.get("/")
def mensagem_de_boas_vindas():
    return {
        "mensagem": "Bem-vindo ao servidor do GigaRoça & Café!",
        "status": "O servidor está online e o Banco de Dados está estruturado!"
    }