import os


class Config:
    print('Config started...')
    SECRET_KEY = os.urandom(21)
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'sogari812@gmail.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
