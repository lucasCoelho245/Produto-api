from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.produto_schemas import ProdutoCreate, ProdutoUpdate, ProdutoRead
from src.services.produto_repo_sqlalchemy import ProdutoRepositorySQLAlchemy


class ProdutoService:
    """Camada de serviço — orquestra regras de negócio entre as rotas e o repositório"""

    def __init__(self, db: Session):
        self.repo = ProdutoRepositorySQLAlchemy(db)

    def listar_produtos(self) -> List[ProdutoRead]:
        return self.repo.listar()

    def buscar_produto(self, produto_id: int) -> Optional[ProdutoRead]:
        return self.repo.buscar_por_id(produto_id)

    def criar_produto(self, produto: ProdutoCreate) -> ProdutoRead:
        return self.repo.criar(produto)

    def atualizar_produto(self, produto_id: int, produto: ProdutoUpdate) -> Optional[ProdutoRead]:
        return self.repo.atualizar(produto_id, produto)
