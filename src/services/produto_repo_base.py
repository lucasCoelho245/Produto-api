from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from src.models.produto import Produto


class ProdutoRepositoryBase(ABC):
    """Contrato para implementação de repositório de produtos."""

    @abstractmethod
    def listar(self) -> List[Produto]:
        raise NotImplementedError

    @abstractmethod
    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        raise NotImplementedError

    @abstractmethod
    def criar(self, nome: str, preco: float, ativo: bool) -> Produto:
        raise NotImplementedError

    @abstractmethod
    def atualizar(self, produto_id: int, nome: str, preco: float, ativo: bool) -> Optional[Produto]:
        raise NotImplementedError

    @abstractmethod
    def remover(self, produto_id: int) -> bool:
        raise NotImplementedError
