from dotenv import load_dotenv
import os

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'the most secure encryption key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SB_MAIL_SUBJECT_PREFIX = ['SB']
    SB_MAIL_SENDER = 'Social Blog Admin <sb@example.com>'
    SB_ADMIN = os.getenv('SB_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
