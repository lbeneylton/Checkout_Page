"""Gerador de sessions"""
# Funções para gerar engine e sessões
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importação do objeto de configuração do banco
from src.app.core.config import settings

URL_DATABASE = settings.database_url

# Definindo a engine
engine = create_engine(
    URL_DATABASE,
    pool_pre_ping=True,  # Faz verificação se a conexão está morta
    echo=True  # True apenas para dev
)

# Defininco a fabrica de sessões, Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
