from pydantic import BaseModel, Field
from typing import Optional


class ProdutoCreate(BaseModel):
    nome: str
    preco: float = Field(gt=0, description="Preço deve ser maior que zero")
    ativo: bool = True


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = Field(default=None, gt=0)
    ativo: Optional[bool] = None


class ProdutoRead(BaseModel):
    id: int
    nome: str
    preco: float
    ativo: bool
    model_config = {"from_attributes": True}