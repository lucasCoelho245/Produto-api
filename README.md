# 📦 API de Produtos

API RESTful para gerenciamento de produtos, construída com **FastAPI**, **SQLAlchemy** e **SQLite**, seguindo arquitetura em camadas.

---

## 🚀 Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.12+ |
| FastAPI | 0.115.0 |
| Uvicorn | 0.30.0 |
| Pydantic | 2.9.0 |
| SQLAlchemy | latest |
| SQLite | embutido |

---

## 📁 Estrutura

```
Produto-api/
├── main.py                             # Exemplo isolado da classe Produto
├── requirements.txt
├── data/                               # Banco SQLite gerado em runtime
└── src/
    ├── main.py                         # Entrypoint — reexporta o app pro uvicorn
    ├── models/
    │   ├── produto.py                  # Domínio (regras de negócio)
    │   ├── produto_db.py               # ORM (mapeamento tabela)
    │   └── produto_schemas.py          # Schemas Pydantic
    ├── services/
    │   ├── produto_repo_base.py        # Contrato abstrato do repositório
    │   └── produto_repo_sqlalchemy.py  # Implementação com SQLAlchemy
    └── utils/
        ├── database.py                 # Engine, Base e sessão
        └── main.py                     # App FastAPI + rotas
```

---

## ⚙️ Como rodar

```bash
# 1. Clone e entre na pasta
git clone <seu-repo>
cd Produto-api

# 2. Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Suba a API
python -m uvicorn src.main:app --reload
```

Acesse: http://localhost:8000/docs

---

## 🔌 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Healthcheck |
| `GET` | `/produtos` | Lista todos |
| `GET` | `/produtos/{id}` | Busca por ID |
| `POST` | `/produtos` | Cria produto |
| `PUT` | `/produtos/{id}` | Atualiza produto |

### Payload (POST)
```json
{
  "nome": "Teclado Mecânico",
  "preco": 350.00,
  "ativo": true
}
```

---

## 🏗️ Arquitetura

```
Requisição HTTP
      │
      ▼
  FastAPI (src/utils/main.py)
      │
      ▼
  Schemas Pydantic  ◄── validação entrada/saída
      │
      ▼
  Modelo de domínio  ◄── regras de negócio
      │
      ▼
  ProdutoRepositoryBase  ◄── contrato abstrato
      │
      ▼
  ProdutoRepositorySQLAlchemy  ◄── implementação concreta
      │
      ▼
  SQLite via SQLAlchemy
```
