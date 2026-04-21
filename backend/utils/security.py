from passlib.context import CryptContext

# Configuração do algoritmo de Hash (BCrypt) para proteger senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)