import pytest
from django.contrib.auth.models import User


def pytest_configure(config):
    config.pluginmanager.set_blocked("pytest_flask")


@pytest.fixture(autouse=True)
def _staticfiles_storage(settings):
    settings.STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"


@pytest.fixture()
def user(db):
    return User.objects.create_user(
        username="admin@example.nhs.uk",
        email="admin@example.nhs.uk",
        password="ChangeMe123!",
        first_name="Admin",
        last_name="User",
    )
