#Здесь прописываются все настройки Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#Создаем объект Flask
app = Flask(__name__)

#Устанавливаем секретный ключ
app.config['SECRET_KEY'] = 'my_very_secret_key_try_to_guess_it'

#Подключаем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#Подключаем систему авторизации
login_manager = LoginManager(app)
login_manager.login_view = 'login'

#Подключаем шифрование паролей
bcrypt = Bcrypt(app)

#Подключаем маршруты
from app import routes