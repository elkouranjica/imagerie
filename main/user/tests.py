import pytest
from main.user.models import User

data_user = {
    "matricule": "123456",
    "password": "test_password"
}


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.matricule == data_user["matricule"]
