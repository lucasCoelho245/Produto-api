class Produto:
    """Classe simples pra testar o modelo fora da API"""

    def __init__(self, nome: str, preco: float):
        self.nome: str = nome
        self.preco: float = preco

    def __str__(self):
        return f"O produto é {self.nome} e o preço é {self.preco}"


p1 = Produto("Teclado", 250.0)
print(p1)
