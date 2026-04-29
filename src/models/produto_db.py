from sqlalchemy import Column, Integer, String, Float, Boolean
from src.utils.database import Base


class ProdutoDB(Base):
    """Mapeamento ORM da tabela produtos"""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)
