class Produto:
    """Modelo de domínio — sem ORM, sem banco, só regra de negócio"""

    def __init__(self, nome: str, preco: float, ativo: bool = True):
        self.nome = nome
        self.preco = preco
        self.ativo = ativo

    def aplicar_desconto(self, percentual: float):
        if not (0 < percentual < 100):
            raise ValueError("Percentual de desconto inválido")
        self.preco -= self.preco * (percentual / 100)

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def __str__(self):
        return f"O produto é {self.nome} e o preço é {self.preco}"
