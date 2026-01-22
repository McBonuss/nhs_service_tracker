import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user(db):
    return User.objects.create_user(
        username="admin@example.nhs.uk",
        email="admin@example.nhs.uk",
        password="ChangeMe123!",
        first_name="Admin",
        last_name="User",
    )
