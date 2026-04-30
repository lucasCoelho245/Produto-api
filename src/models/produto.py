#!/usr/bin/env python3
from __future__ import annotations


class Produto:
    """Modelo de domínio — sem ORM, sem banco, só regra de negócio"""

    def __init__(self, produto_id: int, nome: str, preco: float, ativo: bool = True) -> None:
        self._produto_id: int = produto_id
        self.nome: str = nome
        self._preco: float = 0.0
        self.preco = preco  # usa o setter para validar
        self.ativo: bool = ativo

    def __str__(self) -> str:
        return f"Produto(id={self._produto_id}, nome={self.nome}, preco={self._preco}, ativo={self.ativo})"

    @property
    def id(self) -> int:
        return self._produto_id

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo")
        self._preco = valor

    def aplicar_desconto(self, percentual: float) -> None:
        if not (0 <= percentual < 100):
            raise ValueError("Percentual deve ser entre 0 e 100")
        desconto = self._preco * (percentual / 100)
        self._preco -= desconto

    def ativar(self) -> None:
        self.ativo = True

    def desativar(self) -> None:
        self.ativo = False
