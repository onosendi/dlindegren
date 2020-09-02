import os

from dotenv import load_dotenv

# Load environment variables.
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
