# Importação da Factory Session
from app.database.session import SessionLocal


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
