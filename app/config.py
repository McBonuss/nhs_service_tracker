import os

class BaseConfig:
    # Fixed demo key so the training app runs without external secrets.
    # This project only uses non-sensitive test data.
    SECRET_KEY = "dev-demo-key-not-secret"
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
