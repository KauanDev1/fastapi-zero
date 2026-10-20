from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_zero.database import get_session
from fastapi_zero.models import User

# Importar schemas
from fastapi_zero.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='API que funfa!')

database = []


@app.get('/')
def read_root():
    return {'api_status': 'online'}


# Response model é como a requisição irá retornar para o usuario e status code
# defini qual codigo http deve retornar caso aquela requisição de certo
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
# Metodo de criação como POST precisam receber uma variavel q guardar o valor
# recebido e de um schema(schema é como se fosse um contrato q pré estabelece
# oq precisa ser recebido de dados)
# User é a variavel que armazena os dados recebidos do metodo http, e o
# UserSchema é como os dados devem ser armazenado.
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Usuario ou email já existentes!',
        )

    db_user = User(
        username=user.username, email=user.email, password=user.password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


# Pydantic espera receber um dicionário com a chave chamada 'users' ( o
# schema de resposta é o UserList onde retorna o usuarios como uma lista de
# User) para poder validar e retornar o metdo get
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


# {user_id} é um input para selecionar o usuario q será atualizado, logo para
# ele ser usado na função ele deve ser adicionado dentro do parametros da
# função
@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
# PUT para atualizar ele atualiza todo o usuario, toda a informação de usuario
# bem parecido com o post na logica porem ele mantém o id do usuario
# selecionado para atualização
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário inexistente, adicione um usuário valido!',
        )

    # pega dentro do database o valor do id e subtrai pro 1 para validar a
    # posição do usuario, já q lista começão de 0, 1, 2 e o valor do id
    # do usuario é 1, 2, 3
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def delete_user(user_id: int):
    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário inexistente, adicione um usuário valido!',
        )
    return database.pop(user_id - 1)


@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def read_one_users(user_id: int):
    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário inexistente, adicione um usuário valido!',
        )
    user_with_id = database[user_id - 1]
    return user_with_id
