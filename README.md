# API Simples com Flask - Grupo 1

## Integrantes
- Beatriz Bramont
- Giovanna Petrilli
- Isadora Silva

## Descrição do Projeto
Esta é uma API RESTful simples desenvolvida em Python usando o framework **Flask**, para gerenciar usuários em memória (lista de dicionários).  
O projeto realiza todas as operações **CRUD**: Create, Read, Update e Delete.

---

## Funcionalidades
- **POST /users**: Cria um novo usuário com `nome` e `email`.
- **GET /users**: Lista todos os usuários cadastrados.
- **GET /users/<id>**: Busca um usuário específico pelo ID.
- **PUT /users/<id>**: Atualiza os dados de um usuário existente.
- **DELETE /users/<id>**: Remove um usuário através do ID.

---

## Pré-requisitos

- Python 3.x
- Flask

Instale o Flask via pip:
    pip install flask

---
## Como executar
git clone <nossa_url>
cd AtvAPIsimplesPython
python app.py
curl http://127.0.0.1:5000/users