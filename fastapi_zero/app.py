from http import HTTPStatus


from fastapi import FastAPI
from fastapi_zero.schemas import UserSchema


app = FastAPI(title='API que funfa!')


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserSchema)
def create_user(user: UserSchema):
    return user




