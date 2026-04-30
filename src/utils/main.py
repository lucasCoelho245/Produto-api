from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from src.utils.database import get_db, criar_tabelas
from src.models.produto_schemas import ProdutoCreate, ProdutoUpdate, ProdutoRead
from src.services.produto_service import ProdutoService

# Cria as tabelas no banco na primeira execução
criar_tabelas()

app = FastAPI(title="API de Produtos", version="1.0.0")


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.get("/produtos", response_model=List[ProdutoRead])
def listar_produtos(db: Session = Depends(get_db)):
    return ProdutoService(db).listar_produtos()


@app.get("/produtos/{produto_id}", response_model=ProdutoRead)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = ProdutoService(db).buscar_produto(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/produtos", response_model=ProdutoRead, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return ProdutoService(db).criar_produto(produto)


@app.put("/produtos/{produto_id}", response_model=ProdutoRead)
def atualizar_produto(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    atualizado = ProdutoService(db).atualizar_produto(produto_id, produto)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return atualizado
