from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from core.settings import settings

print(f"--- [DEBUG] Valor de settings.DATABASE_URL: {settings.DATABASE_URL} ---")
print(f"--- [DEBUG] Tipo de settings.DATABASE_URL: {type(settings.DATABASE_URL)} ---")

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
