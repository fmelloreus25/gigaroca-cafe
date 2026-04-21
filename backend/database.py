import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega o .env
load_dotenv()

# Pega a URL do Pooler
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.strip().replace('"', '').replace("'", "")

# Cria o "motor" de conexão
engine = create_engine(DATABASE_URL)

# Cria a fábrica de "sessões" (é como se fosse o caixa do supermercado que atende as vendas)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que usaremos para criar as nossas tabelas
Base = declarative_base()