# Builders Movie API - Desafio

API desenvolvida com **FastAPI** para gerenciar uma lista de filmes favoritos. Inclui autenticação via token, banco de dados SQLite e está empacotada com Docker.

## Tecnologias Utilizadas

- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Docker / Docker Compose

## Instalação local

### 1. Clone o projeto

```bash
git clone https://github.com/vinnyscosta/builders-movie-api.git
cd builders-movie-api
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Rode o servidor
```bash
uvicorn app.main:app --reload
```

Sendo assim, a api estará disponível em Acesse: http://localhost:8000/docs

## Rodando com Docker

### 1. Build e up
```bash
docker-compose up --build
```

### 2. Acesso
Sendo assim, a api estará disponível em Acesse: http://localhost:8000/docs

