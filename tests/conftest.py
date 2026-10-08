import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


# Cria um client para simular requisições http sem precisar subir um
# servidor para fazer os testes, cliente de teste recebe o nome da aplicação
@pytest.fixture
def client():
    return TestClient(app)


# Fixture é uma função q prepara alguma coisa antes do teste rodar e o teste
# recebe ela só colocando o nome dela nos parametros, ex: test_x(session).
# Essa fixture cria um banco de dados novo e limpo pra cada teste, assim um
# teste nao interfere no outro, e depois q o teste acaba ela apaga tudo.
@pytest.fixture
def session():
    # engine é a conexão com o banco de dados, sqlite:///:memory: cria o
    # banco direto na memoria ram, sem criar arquivo, por isso é rapido e
    # some quando o teste termina.
    engine = create_engine('sqlite:///:memory:')
    # metadata guarda todas as tabelas registradas no table_registry (tipo a
    # users), e o create_all cria essas tabelas dentro do banco.
    table_registry.metadata.create_all(engine)

    # Session com S maiusculo é a classe do sqlalchemy, ela só serve pra
    # criar uma sessão ligada no banco (engine). session minusculo é a
    # sessão criada, é ela q faz o add, commit e busca os dados.
    # O with serve pra abrir uma coisa e garantir q ela vai ser fechada,
    # mesmo se der erro no meio. Entao ele abre a session, deixa usar ela
    # dentro do bloco e quando sai do bloco fecha sozinho (session.close()).
    # O as session só da o nome pra sessão criada, pode ser qualquer nome.
    with Session(engine) as session:
        # yield é tipo um return, mas ao inves de acabar a função ele entrega
        # a session pro teste e pausa a fixture aqui. Quando o teste acaba a
        # fixture continua do yield pra baixo. Por isso tudo antes do yield
        # roda antes do teste (preparar) e tudo depois roda depois (limpar).
        # Como o yield ta dentro do with a session fica aberta o teste todo.
        yield session

    # Depois do teste apaga todas as tabelas pra deixar o banco limpo.
    table_registry.metadata.drop_all(engine)
