from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.api_controllers import api
from backend.models import * 

jwt = JWTManager()

def init_app():
    app = Flask(__name__, template_folder='frontend/templates')
    
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///home.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # Set a secure key for JWT
    app.app_context().push()
    db.init_app(app)
    jwt.init_app(app)
    api.init_app(app)  # Initialize your API routes if needed
    with app.app_context():  # Push the app context after initializing db
        db.create_all()
    return app

app = init_app()  # This will initialize your app correctly

from backend.controllers import * 


if __name__ == "__main__":
    app.run(debug=True)
