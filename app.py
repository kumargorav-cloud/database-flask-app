from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='templates')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'


    app.secret_key = 'some key'
    login_manager = LoginManager()
    login_manager.init_app(app)


    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    def unauthorized_access():
        return redirect(url_for('index'))


    bcrypt = Bcrypt()



    db.init_app(app)

    from routes import register_routes
    register_routes(app, db,bcrypt)
    # after doing we will run in terminal
    # flask db init --to initialize the db
    #flask db migrate--to send the table 
    #flask db upgrade--if there is any change in table you made

    migrate = Migrate(app,db)

    return app