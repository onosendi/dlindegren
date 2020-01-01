'''
    config
    ~~~~~~

    Flask configuration file.
'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class BaseConfig:
    ''' Base configurations.

    These are the base configurations that will be loaded, unless otherwise
    overridden.

    ..note: Never load this configuration directly.
    '''
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'


class DefaultConfig(BaseConfig):
    ''' Default configurations. '''
    DEBUG = True


class ProductionConfig(BaseConfig):
    ''' Production configurations. '''
