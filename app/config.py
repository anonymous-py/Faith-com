import os


class Config:
    SECRET_KEY = os.environ.get('secret_key') or 'mnsduihsfuioshnifojsiofhiusdnsduihsuhfythindjbiudhvnfuihurw'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE') or 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_MODIFICATIONS = False
