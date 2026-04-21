from pydantic import BaseModel
from typing import Optional

# --- Store Schemas ---
class StoreBase(BaseModel):
    name: str
    address: Optional[str] = None

class StoreResponse(StoreBase):
    id: int

    class Config:
        from_attributes = True

# --- User Schemas ---
class UserBase(BaseModel):
    full_name: str
    email: str
    role: str

class UserResponse(UserBase):
    id: int
    store_id: Optional[int] = None

    class Config:
        from_attributes = True

# --- Product Schemas ---
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    cost_price: float
    sale_price: float

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True