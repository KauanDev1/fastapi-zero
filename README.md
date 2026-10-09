<div align="center">

# 🚀 FastAPI do Zero

**Projeto de estudos construído acompanhando o curso _FastAPI do Zero_,  
do [Eduardo Mendes — `dunossauro`](https://www.youtube.com/@Dunossauro) 🦖**

<br>

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.13-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.1-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-1.20-6BA81E?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)

<br>

`status:` **em andamento** 🛠️ &nbsp;•&nbsp; `progresso:` **4 / 15 aulas**

▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱

</div>

---

## 📖 Sobre o projeto

Este repositório é o meu caderno de código do curso **FastAPI do Zero**.

A ideia não é só ter uma API funcionando no final, mas **entender cada linha pelo caminho**:
por que o Pydantic valida daquele jeito, por que o teste é escrito antes, por que a estrutura
de pastas muda na metade do curso. Tudo é digitado, quebrado, consertado e testado à mão —
aula por aula, commit por commit.

No fim do curso, o projeto vira uma API completa de gerenciamento de tarefas, com:

- CRUD de usuários e de tarefas
- Autenticação e autorização com **JWT**
- Banco de dados com **SQLAlchemy** + migrações com **Alembic**
- Testes automatizados com **pytest** e cobertura de código
- **Docker** + **PostgreSQL**
- **CI** no GitHub Actions e deploy em produção

---

## 🎓 Sobre o curso

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| 🎤 **Instrutor**  | Eduardo Mendes (`dunossauro`)                                                    |
| 📚 **Material**   | [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com/)            |
| 📺 **Aulas**      | [YouTube — @Dunossauro](https://www.youtube.com/@Dunossauro)                      |
| 💰 **Preço**      | Gratuito, aberto e feito com muito carinho pela comunidade Python BR              |

> Curso excelente e **100% gratuito**. Se ele te ajudou, considere apoiar o trabalho do Dunossauro. 💜

---

## 🧰 Stack

| Ferramenta        | Para quê                                              |
| ----------------- | ----------------------------------------------------- |
| **FastAPI**       | Framework web assíncrono da API                       |
| **Pydantic**      | Validação e serialização dos dados (schemas)          |
| **SQLAlchemy**    | ORM: mapeia as classes Python para tabelas do banco   |
| **Alembic**       | Migrações do banco de dados                           |
| **pydantic-settings** | Lê as configurações (ex.: `DATABASE_URL`) do `.env` |
| **SQLite**        | Banco de dados usado em desenvolvimento e nos testes  |
| **Poetry**        | Gerenciamento de dependências e do ambiente virtual   |
| **Pytest**        | Testes automatizados                                  |
| **pytest-cov**    | Relatório de cobertura de testes                      |
| **Ruff**          | Linter e formatador                                   |
| **Taskipy**       | Atalhos para os comandos do dia a dia                 |

---

## 📂 Estrutura do projeto

```
fastapi_zero/
├── fastapi_zero/
│   ├── __init__.py
│   ├── app.py          # rotas da aplicação
│   ├── models.py       # tabelas do banco (SQLAlchemy)
│   ├── schemas.py      # modelos de entrada e saída (Pydantic)
│   └── settings.py     # configurações lidas do .env
├── migrations/
│   ├── env.py          # liga o Alembic aos models e ao .env
│   └── versions/       # uma migração por arquivo
├── tests/
│   ├── __init__.py
│   ├── conftest.py     # fixtures (client, session, mock de data)
│   ├── test_app.py     # testes das rotas
│   └── test_db.py      # testes do banco de dados
├── alembic.ini         # configuração do Alembic
├── ALEMBIC.md          # guia rápido de comandos do Alembic
├── pyproject.toml      # dependências, lint e tasks
└── README.md
```

---

## ⚙️ Como rodar

**Pré-requisitos:** Python `3.14+` e [Poetry](https://python-poetry.org/).

```bash
# 1. clone o repositório
git clone https://github.com/KauanDev1/fastapi_zero.git
cd fastapi_zero

# 2. instale as dependências
poetry install

# 3. crie o arquivo .env com a URL do banco
echo 'DATABASE_URL="sqlite:///database.db"' > .env

# 4. crie as tabelas aplicando as migrações
poetry run alembic upgrade head

# 5. suba o servidor
poetry run task run
```

> 💡 Se preferir ativar o ambiente virtual antes, use `poetry env activate`
> (ou `poetry shell`, nas versões antigas do Poetry) e depois só `task run`.

A API sobe em **http://localhost:8000** 🎉

| Endereço                                                   | O que é                        |
| ---------------------------------------------------------- | ------------------------------ |
| [`/`](http://localhost:8000/)                               | Rota raiz                      |
| [`/docs`](http://localhost:8000/docs)                       | Documentação interativa Swagger |
| [`/redoc`](http://localhost:8000/redoc)                     | Documentação ReDoc             |

---

## 🧪 Testes e qualidade

Os atalhos ficam no `pyproject.toml`, via **taskipy**:

| Comando        | O que faz                                              |
| -------------- | ------------------------------------------------------ |
| `task run`     | Sobe o servidor em modo desenvolvimento                |
| `task test`    | Roda o lint e depois os testes com cobertura           |
| `task lint`    | Procura problemas no código                            |
| `task format`  | Corrige e formata o código                             |

Depois de `task test`, o relatório de cobertura em HTML fica em `htmlcov/index.html`.

Os testes de banco **não usam o `database.db`**: cada teste cria um SQLite novo
na memória, com as tabelas criadas na hora, e apaga tudo no final.

---

## 🗄️ Migrações

O banco é versionado com **Alembic**. O fluxo de sempre:

```bash
# depois de alterar fastapi_zero/models.py
alembic revision --autogenerate -m "descrição da mudança"   # gera a migração
alembic upgrade head                                          # aplica no banco
```

Os outros comandos e os cuidados com o autogenerate estão no [`ALEMBIC.md`](ALEMBIC.md).

---

## 📺 Progresso das aulas

**Legenda:** ✅ finalizada &nbsp;•&nbsp; 🟡 assistindo &nbsp;•&nbsp; ⬜ ainda não concluída

| #      | Aula                                                            | Status |
| :----: | --------------------------------------------------------------- | :----: |
| **01** | Configurando o ambiente de desenvolvimento                       |   ✅   |
| **02** | Introdução ao desenvolvimento WEB                                |   ✅   |
| **03** | Estruturando o projeto e criando rotas CRUD                      |   ✅   |
| **04** | Configurando o banco de dados e gerenciando migrações com Alembic |   ✅   |
| **05** | Integrando banco de dados à API                                  |   🟡   |
| **06** | Autenticação e Autorização com JWT                               |   ⬜   |
| **07** | Refatorando a estrutura do projeto                               |   ⬜   |
| **08** | Tornando o projeto assíncrono                                    |   ⬜   |
| **09** | Tornando o sistema de autenticação robusto                       |   ⬜   |
| **10** | Criando rotas CRUD para gerenciamento de tarefas                 |   ⬜   |
| **11** | Containerizando a aplicação e introduzindo o PostgreSQL          |   ⬜   |
| **12** | Automatizando os testes com Integração Contínua (CI)             |   ⬜   |
| **13** | Fazendo deploy no Fly.io                                         |   ⬜   |
| **14** | Despedida e próximos passos                                      |   ⬜   |
| **15** | Projeto final                                                    |   ⬜   |

<div align="center">

**4 finalizadas** &nbsp;•&nbsp; **1 em andamento** &nbsp;•&nbsp; **10 pela frente**

</div>

---

## 🤖 Sobre o uso de IA

> [!IMPORTANT]
> **Todo o curso foi feito na mão.**
>
> Cada rota, cada schema, cada teste deste repositório foi escrito por mim, acompanhando as
> aulas, sem código gerado ou copiado de IA.
>
> A ajuda de IA foi usada **apenas para tirar dúvidas e entender melhor alguns conceitos**,
> do mesmo jeito que se usa a documentação, o Stack Overflow ou uma conversa com um colega.
>
> Os **únicos** artefatos deste repositório escritos por IA são **este README** e o
> guia de comandos **`ALEMBIC.md`**.

---

<div align="center">

Feito com ☕, `pytest` e muita paciência por **[Kauan](https://github.com/KauanDev1)**

</div>
