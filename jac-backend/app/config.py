import os

# Base configuration (shared by all environments)
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")  
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///mydb.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")


# Development environment
class DevelopmentConfig(Config):
    DEBUG = True


# Production environment
class ProductionConfig(Config):
    DEBUG = False


# Testing environment
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
