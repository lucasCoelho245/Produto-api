from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.produto_db import ProdutoDB
from src.models.produto_schemas import ProdutoCreate, ProdutoUpdate, ProdutoRead
from src.services.produto_repo_base import ProdutoRepositoryBase


class ProdutoRepositorySQLAlchemy(ProdutoRepositoryBase):
    """Implementação do repositório usando SQLAlchemy + SQLite"""

    def __init__(self, db: Session):
        self.db = db

    def listar(self) -> List[ProdutoRead]:
        produtos = self.db.query(ProdutoDB).all()
        return [ProdutoRead.model_validate(p) for p in produtos]

    def buscar_por_id(self, produto_id: int) -> Optional[ProdutoRead]:
        produto = self.db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if not produto:
            return None
        return ProdutoRead.model_validate(produto)

    def criar(self, produto: ProdutoCreate) -> ProdutoRead:
        novo = ProdutoDB(**produto.model_dump())
        self.db.add(novo)
        self.db.commit()
        self.db.refresh(novo)
        return ProdutoRead.model_validate(novo)

    def atualizar(self, produto_id: int, produto: ProdutoUpdate) -> Optional[ProdutoRead]:
        existente = self.db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if not existente:
            return None

        # Atualiza só os campos que foram enviados
        for campo, valor in produto.model_dump(exclude_unset=True).items():
            setattr(existente, campo, valor)

        self.db.commit()
        self.db.refresh(existente)
        return ProdutoRead.model_validate(existente)