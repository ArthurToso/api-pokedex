<div align="center">

# ⚡ Pokédex API

**REST API completa para o aplicativo Android da Pokédex**  
Desenvolvida com FastAPI · SQLite · JWT Auth

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)

</div>

---

## 📖 Sobre o Projeto

Este repositório contém o **back-end** do aplicativo Android de Pokédex, desenvolvido como projeto acadêmico em grupo na faculdade. **A API foi inteiramente desenvolvida por mim**, enquanto os outros integrantes do grupo ficaram responsáveis pelo aplicativo Android em Kotlin.

A API oferece autenticação segura com JWT e operações completas de CRUD para gerenciamento de Pokémons, servindo como camada de dados do app mobile.

> 🎓 Projeto acadêmico · API desenvolvida individualmente · Parte do meu portfólio de desenvolvimento back-end

---

## 🏗️ Arquitetura

```
pokedex-api/
├── main.py        # Rotas e endpoints da API
├── models.py      # Modelos do banco de dados (SQLAlchemy)
├── schemas.py     # Validação de dados (Pydantic)
├── auth.py        # Autenticação JWT e hashing de senhas
└── .env           # Variáveis de ambiente (não versionado)
```

---

## ✨ Funcionalidades

- 🔐 **Autenticação JWT** — Login seguro com tokens Bearer e hashing bcrypt
- 📋 **CRUD completo de Pokémons** — Criar, listar, buscar, editar e deletar
- 🔍 **Busca por tipo e habilidade** — Filtros via SQL `LIKE` para busca parcial
- 👤 **Pokémons por treinador** — Cada Pokémon é vinculado ao usuário que o cadastrou
- ✅ **Validação automática** — Schemas Pydantic garantem a integridade dos dados
- 📄 **Docs interativa** — Swagger UI disponível em `/docs` automaticamente

---

## 🚀 Endpoints

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `POST` | `/token` | Login e geração do token JWT | ❌ |
| `POST` | `/pokemons` | Cadastrar novo Pokémon | ✅ |
| `GET` | `/pokemons-list` | Listar todos os Pokémons | ✅ |
| `GET` | `/pokemons/{id}` | Buscar Pokémon por ID | ✅ |
| `GET` | `/pokemons/search/tipo?q=` | Filtrar por tipo | ✅ |
| `GET` | `/pokemons/search/habilidade?q=` | Filtrar por habilidade | ✅ |
| `PUT` | `/pokemons/{id}` | Atualizar dados do Pokémon | ✅ |
| `DELETE` | `/pokemons/{id}` | Remover Pokémon | ✅ |

---

## ⚙️ Como Rodar Localmente

### Pré-requisitos
- Python 3.11+

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/pokedex-api.git
cd pokedex-api

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
echo "SECRET_KEY=sua_chave_secreta_aqui" > .env

# 5. Inicie o servidor
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`  
Documentação interativa: `http://127.0.0.1:8000/docs`

---

## 🔐 Exemplo de Uso

**1. Fazer login e obter token:**
```bash
curl -X POST "http://127.0.0.1:8000/token" \
  -H "Content-Type: application/json" \
  -d '{"username": "ash", "password": "pikachu123"}'
```

**2. Cadastrar um Pokémon (com token):**
```bash
curl -X POST "http://127.0.0.1:8000/pokemons" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Pikachu",
    "tipo": "Elétrico",
    "habilidades": ["Choque do Trovão", "Investida", "Agilidade"]
  }'
```

---

## 🛠️ Tech Stack

| Tecnologia | Uso |
|------------|-----|
| **FastAPI** | Framework web assíncrono e de alta performance |
| **SQLAlchemy** | ORM para mapeamento objeto-relacional |
| **SQLite** | Banco de dados leve para desenvolvimento |
| **Pydantic v2** | Validação e serialização de dados |
| **python-jose** | Geração e verificação de tokens JWT |
| **Passlib + bcrypt** | Hashing seguro de senhas |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |

---

> 📱 Repositório do app Android: [ArthurToso/Pokedex](https://github.com/ArthurToso/Pokedex)  
> Os commits **deste** repositório refletem exclusivamente o meu trabalho individual no back-end.

---

<div align="center">

</div>