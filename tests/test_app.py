from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


# Cria o teste
def test_create_user(client):
    # Cria a requisição que o cliente vai usar para fazer o teste, como a rota
    # testada é a rota users q usa o metodo post. ele recebe o parametros
    # json={} q é os dados q serao enviados no teste
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    # Aqui serve para validar a resposta do teste, validar se resposta da
    # requisição enviada para teste foi o codigo q deve ser retornado e se
    # resposta retornada veio no formato correto
    # obs: Assert serve para validar se algo está correto
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }
