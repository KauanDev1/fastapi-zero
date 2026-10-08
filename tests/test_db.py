from fastapi_zero.models import User
from sqlalchemy import select

def test_create_user(session):
    new_user = User(username='test', email='test@test.com', password='password')

    session.add(new_user)
    session.commit()
    user = session.scalar(
        select(User).where(User.username == 'test')
    )

    assert user.username == 'test'