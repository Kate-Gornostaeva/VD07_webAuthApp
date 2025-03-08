#Декораторы маршрутов, необходимых на сайте
from flask import render_template, request, redirect, url_for
import flask_login
from flask_login import login_user, logout_user, login_required, current_user, login_required
from app import models, forms
from app.models import User
from app.forms import LoginForm, RegistrationForm
from app import bcrypt

#Создаем маршрут для главной страницы
@app.route('/')
def home():
    return render_template('home.html')

#Создаем маршрут для страницы регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегестрировались', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Создаем маршрут для страницы авторизации
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Неправильный логин или пароль', 'danger')
    return render_template('login.html', title='Login', form=form)

#Создаем маршрут для страницы выхода
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

#Создаем маршрут для страницы профиля
@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

