# Importação da Factory Session
from infra.database.session import SessionLocal


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
