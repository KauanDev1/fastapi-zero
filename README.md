<div align="center">

# 🚀 FastAPI do Zero

**Projeto de estudos construído acompanhando o curso _FastAPI do Zero_,  
do [Eduardo Mendes — `dunossauro`](https://www.youtube.com/@Dunossauro) 🦖**

<br>

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.13-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)

<br>

`status:` **em andamento** 🛠️ &nbsp;•&nbsp; `progresso:` **2 / 15 aulas**

▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱

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
│   └── schemas.py      # modelos de entrada e saída (Pydantic)
├── tests/
│   ├── __init__.py
│   └── test_app.py     # testes das rotas
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

# 3. suba o servidor
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

---

## 📺 Progresso das aulas

**Legenda:** ✅ finalizada &nbsp;•&nbsp; 🟡 assistindo &nbsp;•&nbsp; ⬜ ainda não concluída

| #      | Aula                                                            | Status |
| :----: | --------------------------------------------------------------- | :----: |
| **01** | Configurando o ambiente de desenvolvimento                       |   ✅   |
| **02** | Introdução ao desenvolvimento WEB                                |   ✅   |
| **03** | Estruturando o projeto e criando rotas CRUD                      |   ✅   |
| **04** | Configurando o banco de dados e gerenciando migrações com Alembic |   🟡   |
| **05** | Integrando banco de dados à API                                  |   ⬜   |
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

**2 finalizadas** &nbsp;•&nbsp; **1 em andamento** &nbsp;•&nbsp; **12 pela frente**

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
> O **único** artefato deste repositório escrito por IA é **este README**.

---

<div align="center">

Feito com ☕, `pytest` e muita paciência por **[Kauan](https://github.com/KauanDev1)**

</div>
