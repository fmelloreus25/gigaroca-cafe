import os
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import models
import schemas
from database import engine, SessionLocal

# Carrega as variáveis do .env
load_dotenv()

# Inicializa a API
app = FastAPI(
    title="API - GigaRoça & Café",
    description="Sistema de Gestão, Estoque e PDV",
    version="1.0.0"
)

# Injeção de Dependência: Abre e fecha o banco com segurança
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_root():
    return {
        "message": "Welcome to GigaRoça & Café API!",
        "status": "Server is online."
    }

# --- NOSSAS ROTAS DA API ---

# 1. Listar todos os Usuários
@app.get("/api/users", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# 2. Listar todos os Produtos
@app.get("/api/products", response_model=list[schemas.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

# 3. Listar todas as Lojas
@app.get("/api/stores", response_model=list[schemas.StoreResponse])
def get_all_stores(db: Session = Depends(get_db)):
    stores = db.query(models.Store).all()
    return stores

# 4. Cadastrar um novo Produto (POST)
# O status_code=201 significa "Criado com Sucesso" no padrão da web
@app.post("/api/products", response_model=schemas.ProductResponse, status_code=201)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    # Transforma os dados validados pelo Pydantic em um formato que o banco entende
    new_product = models.Product(**product.model_dump())
    
    # Salva no banco de dados
    db.add(new_product)
    db.commit()
    db.refresh(new_product) # Atualiza para pegar o ID que o Supabase gerou
    
    return new_product