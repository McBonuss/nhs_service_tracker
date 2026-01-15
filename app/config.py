import os


class BaseConfig:
    """Base configuration shared across environments.

    Values can be overridden via environment variables loaded from the
    project-level "env" file (see setup.ps1) or the host environment.
    """

    # Allow overriding the secret key from the environment while keeping
    # a sensible default for tests and quick local runs.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-demo-key-not-secret")

    # Prefer DATABASE_URL from the environment; fall back to a local dev DB.
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///dev.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_TIME_LIMIT = None

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    DEBUG = False

def get_config(name=None):
    env = name or os.environ.get("FLASK_ENV", "development")
    mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    return mapping.get(env, DevelopmentConfig)
