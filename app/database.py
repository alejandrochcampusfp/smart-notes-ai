from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de datos SQLite local para persistencia automática de notas
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

# Configuramos el motor de la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para obtener la sesión de base de datos de forma segura
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()