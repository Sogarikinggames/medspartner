from flask import Flask
from .config import Config
from flask_mail import Mail

mail = Mail()

def create_app():
    print("Initializing the app...") 
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mail.init_app(app)

    # Blueprint登録
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
