from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabela das Lojas (A loja principal e as parceiras)
class Loja(Base):
    __tablename__ = "lojas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    endereco = Column(String, nullable=True)
    
    # Relações (Uma loja tem muitos usuários e muito estoque)
    usuarios = relationship("Usuario", back_populates="loja")
    estoques = relationship("Estoque", back_populates="loja")

# Tabela dos Usuários (Seu login, dos gerentes e dos vendedores)
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String) # No futuro vamos criptografar isso!
    papel = Column(String) # Pode ser: 'diretor', 'gerente' ou 'vendedor'
    
    # Se for gerente ou vendedor, a qual loja ele pertence?
    loja_id = Column(Integer, ForeignKey("lojas.id"), nullable=True)
    loja = relationship("Loja", back_populates="usuarios")

# Tabela dos Produtos (Queijos, Doces de Leite, Cafés...)
class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, nullable=True)
    preco_custo = Column(Float)
    preco_venda = Column(Float)
    
    estoques = relationship("Estoque", back_populates="produto")

# Tabela de Estoque (Controla onde está cada produto)
class Estoque(Base):
    __tablename__ = "estoque"
    
    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer, default=0)
    
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    produto = relationship("Produto", back_populates="estoques")
    
    loja_id = Column(Integer, ForeignKey("lojas.id"))
    loja = relationship("Loja", back_populates="estoques")