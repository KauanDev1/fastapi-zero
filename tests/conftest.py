import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


# Cria um client para simular requisições http sem precisar subir um
# servidor para fazer os testes, cliente de teste recebe o nome da aplicação
@pytest.fixture
def client():
    return TestClient(app)
