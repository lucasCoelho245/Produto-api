from __future__ import annotations

from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProdutoDB(Base):
    """
    Modelo ORM para tabela produtos
    """

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"ProdutoDB(id={self.id}, nome={self.nome}, preco={self.preco}, ativo={self.ativo})"
