from abc import ABC, abstractmethod
from typing import List, Optional
from src.models.produto_schemas import ProdutoCreate, ProdutoUpdate, ProdutoRead


class ProdutoRepositoryBase(ABC):
    """Interface que qualquer repositório de produto deve implementar"""

    @abstractmethod
    def listar(self) -> List[ProdutoRead]:
        pass

    @abstractmethod
    def buscar_por_id(self, produto_id: int) -> Optional[ProdutoRead]:
        pass

    @abstractmethod
    def criar(self, produto: ProdutoCreate) -> ProdutoRead:
        pass

    @abstractmethod
    def atualizar(self, produto_id: int, produto: ProdutoUpdate) -> Optional[ProdutoRead]:
        pass