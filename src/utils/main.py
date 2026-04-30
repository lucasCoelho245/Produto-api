from __future__ import annotations

from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from src.models.produto_schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
from src.services.produto_repo_sqlalchemy import ProdutoRepositorySQLAlchemy
from src.services.produto_service import ProdutoService
from src.utils.database import criar_tabela, get_db

app = FastAPI(
    title="Api de Produtos",
    version="2.0.0",
    description="Api para cadastro de produtos",
)

criar_tabela()


@app.get("/", tags=["healthcheck"])
def read_root():
    return {"mensagem": "Api de produtos está no ar. Acesse /docs para ver a documentação Swagger da api"}


@app.get("/produtos", response_model=List[ProdutoRead], tags=["produtos"])
def listar_produtos(db: Session = Depends(get_db)):
    repo = ProdutoRepositorySQLAlchemy(db)
    produto_service = ProdutoService(repo)
    produtos = produto_service.listar_produtos()
    return [ProdutoRead(id=p.id, nome=p.nome, preco=p.preco, ativo=p.ativo) for p in produtos]


@app.get("/produtos/{produto_id}", response_model=ProdutoRead, tags=["produtos"])
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    repo = ProdutoRepositorySQLAlchemy(db)
    produto_service = ProdutoService(repo)
    produto = produto_service.obter_produto(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não foi encontrado")
    return produto


# criar produto
@app.post("/produtos", response_model=ProdutoRead, status_code=status.HTTP_201_CREATED, tags=["produtos"])
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    repo = ProdutoRepositorySQLAlchemy(db)
    produto_service = ProdutoService(repo)
    produto = produto_service.criar_produto(nome=dados.nome, preco=dados.preco, ativo=dados.ativo)
    return ProdutoRead(id=produto.id, nome=produto.nome, preco=produto.preco, ativo=produto.ativo)


# atualizar produto
@app.put("/produtos/{produto_id}", response_model=ProdutoRead, tags=["produtos"])
def atualizar_produto(produto_id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    repo = ProdutoRepositorySQLAlchemy(db)
    produto_service = ProdutoService(repo)

    produto_existente = produto_service.obter_produto(produto_id)
    if not produto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não foi encontrado")

    nome: str = dados.nome if dados.nome is not None else produto_existente.nome
    preco: float = dados.preco if dados.preco is not None else produto_existente.preco
    ativo: bool = dados.ativo if dados.ativo is not None else produto_existente.ativo

    produto_atualizado = produto_service.atualizar_produto(
        produto_id=produto_existente.id,
        nome=nome,
        preco=preco,
        ativo=ativo,
    )
    if not produto_atualizado:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar")
    return ProdutoRead(id=produto_atualizado.id, nome=produto_atualizado.nome, preco=produto_atualizado.preco, ativo=produto_atualizado.ativo)


# remover produto
@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["produtos"])
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    repo = ProdutoRepositorySQLAlchemy(db)
    produto_service = ProdutoService(repo)
    removido = produto_service.remover_produto(produto_id)
    if not removido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não foi encontrado")
