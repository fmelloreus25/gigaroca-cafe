from database import SessionLocal
from models import Store, User
from utils.security import get_password_hash

def run_seed():
    db = SessionLocal()
    
    try:
        # 1. Verifica se a loja matriz já existe (para não duplicar)
        main_store = db.query(Store).filter(Store.name == "GigaRoça Matriz").first()
        
        if not main_store:
            # Cria a loja matriz
            main_store = Store(name="GigaRoça Matriz", address="Centro, Itaguaí - RJ")
            db.add(main_store)
            db.commit()
            db.refresh(main_store)
            print("Successfully created Store: GigaRoça Matriz")
        else:
            print("Store already exists.")

        # 2. Verifica se o seu usuário já existe
        director_email = "fmelloreus25@gmail.com"
        director = db.query(User).filter(User.email == director_email).first()
        
        if not director:
            # Cria o seu perfil atrelado à loja matriz, com a senha criptografada!
            director = User(
                full_name="Fernando Mello",
                email=director_email,
                hashed_password=get_password_hash("Fer250791fer"), 
                role="director",
                store_id=main_store.id
            )
            db.add(director)
            db.commit()
            print("Successfully created Director Profile.")
        else:
            print("Director Profile already exists.")

    except Exception as e:
        print(f"Error during database seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()