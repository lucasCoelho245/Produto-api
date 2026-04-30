from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.produto import Produto
from src.models.produto_db import ProdutoDB
from src.services.produto_repo_base import ProdutoRepositoryBase


class ProdutoRepositorySQLAlchemy(ProdutoRepositoryBase):
    """Implementação do repositório utilizando SQLAlchemy + SQLite"""

    def __init__(self, db: Session):
        self.db = db

    def db_to_entity(self, produto_db: ProdutoDB) -> Produto:
        """Converte modelo ORM para a entidade Produto"""
        return Produto(
            produto_id=produto_db.id,
            nome=produto_db.nome,
            preco=produto_db.preco,
            ativo=produto_db.ativo,
        )

    def listar(self) -> List[Produto]:
        produtos_db = self.db.query(ProdutoDB).all()
        # select * from produtos
        return [self.db_to_entity(p) for p in produtos_db]

    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        produto_db = self.db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        # select * from produtos where id = produto_id
        if not produto_db:
            return None
        return self.db_to_entity(produto_db)

    def criar(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        produto_db = ProdutoDB(nome=nome, preco=preco, ativo=ativo)
        self.db.add(produto_db)
        # INSERT INTO produtos (nome, preco, ativo) values (nome, preco, ativo)
        self.db.commit()
        self.db.refresh(produto_db)
        return self.db_to_entity(produto_db)

    def atualizar(self, produto_id: int, nome: str, preco: float, ativo: bool) -> Optional[Produto]:
        produto_db = self.db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if not produto_db:
            return None
        produto_db.nome = nome
        produto_db.preco = preco
        produto_db.ativo = ativo
        # update produtos set nome=nome, preco=preco, ativo=ativo where id=produto_id
        self.db.commit()
        self.db.refresh(produto_db)
        return self.db_to_entity(produto_db)

    def remover(self, produto_id: int) -> bool:
        produto_db = self.db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        # select * from produtos where id=produto_id
        if not produto_db:
            return False
        self.db.delete(produto_db)
        # delete from produtos where id=produto_id
        self.db.commit()
        return True
