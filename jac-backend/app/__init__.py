from flask import Flask
from .extensions import db, bcrypt, migrate
from .controllers.excel_controller import excel_bp

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'super-secret-key'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprint
    app.register_blueprint(excel_bp)

    return app
