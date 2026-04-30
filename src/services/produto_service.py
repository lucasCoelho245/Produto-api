from __future__ import annotations

from typing import List, Optional

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepositoryBase


class ProdutoService:
    """Camada de serviço para orquestrar operações de produtos."""

    def __init__(self, repo: ProdutoRepositoryBase):
        self.repo = repo

    def listar_produtos(self) -> List[Produto]:
        return self.repo.listar()

    def obter_produto(self, produto_id: int) -> Optional[Produto]:
        return self.repo.buscar_por_id(produto_id)

    def criar_produto(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        return self.repo.criar(nome=nome, preco=preco, ativo=ativo)

    def atualizar_produto(
        self,
        produto_id: int,
        nome: str,
        preco: float,
        ativo: bool,
    ) -> Optional[Produto]:
        return self.repo.atualizar(produto_id, nome=nome, preco=preco, ativo=ativo)

    def remover_produto(self, produto_id: int) -> bool:
        return self.repo.remover(produto_id)
