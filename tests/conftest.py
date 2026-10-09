from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
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


# O @contextmanager deixa uma função com yield ser usada no with. A fixture
# session nao precisa dele pq quem cuida do yield dela é o pytest, mas essa
# função quem chama é o proprio teste, entao quem cuida do yield é o with.
# Ela serve pra forçar uma data fixa no created_at, pq normalmente quem
# preenche ele é o banco (func.now()) e no teste nao da pra saber a data
# exata pra comparar. model é a tabela (ex: User) e time é a data fixa.
@contextmanager
def _mock_db_time(model, time=datetime(2025, 5, 20)):
    # hook é uma função q o sqlalchemy chama sozinho quando acontece algo.
    # target é o objeto q vai ser salvo (ex: o user), se ele tiver
    # created_at coloca a data fixa nele. mapper e connection o sqlalchemy
    # manda junto mas aqui nao são usados.
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time

    # Liga o hook, fala pro sqlalchemy q antes de inserir (before_insert)
    # um model no banco é pra rodar o fake_time_hook.
    event.listen(model, 'before_insert', fake_time_hook)

    # Entrega a data pro teste e pausa aqui, igual na fixture session.
    # Quando sai do with a função continua do yield pra baixo.
    yield time

    # Desliga o hook pra nao afetar os outros testes.
    event.remove(model, 'before_insert', fake_time_hook)


# Fixture q entrega a função _mock_db_time pro teste, sem os parenteses ela
# nao chama a função, só entrega ela. Assim o teste chama do jeito q quiser
# escolhendo o model e a data, ex: with mock_db_time(model=User) as time:
@pytest.fixture
def mock_db_time():
    return _mock_db_time
