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
    SERVER_NAME = 'dlindegren.local:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI' 
    RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DefaultConfig(BaseConfig):
    ''' Default configurations. '''
    DEBUG = True


class ProductionConfig(BaseConfig):
    ''' Production configurations. '''
    SERVER_NAME = 'dlindegren.com'
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_SITE') or 'secret'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_SECRET') or 'secret'
