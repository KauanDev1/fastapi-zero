from http import HTTPStatus

from fastapi import FastAPI

# Importar schemas
from fastapi_zero.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='API que funfa!')

database = []


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}


# Response model é como a requisição irá retornar para o usuario e status code
# defini qual codigo http deve retornar caso aquela requisição de certo
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
# Metodo de criação como POST precisam receber uma variavel q guardar o valor
# recebido e de um schema(schema é como se fosse um contrato q pré estabelece
# oq precisa ser recebido de dados)
# User é a variavel que armazena os dados recebidos do metodo http, e o 
# UserSchema é como os dados devem ser armazenado.
def create_user(user: UserSchema):
    # user_with_id é uma variavel q cria o usuario com id para adicionar-lo ao
    # database, ele usa a função UserDB que é o contrato de input o userschema 
    # com id, dai ele descompacta com a função **model_dump() q fica igual o 
    # trem ali, e add o user q veio do input e poe só um id nele.
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    # Model dump faz o trabalho braçal de:         username=user.username,
    #                                              email=user.email,
    #                                              password=user.password,
    # pro dev nao precisar escrever na mão.

    # add o usuario no banco de dados ficticio.
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    database[user_id - 1] = user_with_id

    return user_with_id
