from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Store(Base):
    __tablename__ = "stores"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, nullable=True)
    
    users = relationship("User", back_populates="store")
    inventories = relationship("Inventory", back_populates="store")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String) # 'director', 'manager', 'seller'
    
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=True)
    store = relationship("Store", back_populates="users")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    cost_price = Column(Float)
    sale_price = Column(Float)
    
    inventories = relationship("Inventory", back_populates="product")

class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, default=0)
    
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="inventories")
    
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="inventories")