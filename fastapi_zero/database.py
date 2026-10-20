from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_zero.settings import Settings

# engine é a conexão com o banco de dados. Ele precisa saber ONDE o banco
# está, e quem sabe isso é o .env. O Settings() lê o .env e o .DATABASE_URL
# pega o valor 'sqlite:///database.db'. É igual ao engine do conftest, só q
# lá era o banco na memoria (:memory:) e aqui é o banco de verdade (arquivo).
# Ele fica fora da função pq a conexão é criada uma vez só, quando a api
# sobe, e todas as requisições usam a mesma.
engine = create_engine(Settings().DATABASE_URL)


# Essa função entrega uma session (o "carrinho" q faz add, commit e busca)
# pra cada requisição. Quem vai chamar ela é o FastAPI, pelo Depends, no
# passo 2. Funciona igual a fixture session do conftest:
def get_session():
    # O with abre a session ligada no banco (engine) e garante q ela vai ser
    # fechada no final, mesmo se a rota der erro.
    with Session(engine) as session:
        # yield entrega a session pra rota e pausa aqui. Quando a rota
        # termina, a função continua, sai do with e a session é fechada.
        yield session
