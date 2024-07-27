from . import auth
from flask import render_template, redirect, request, flash, url_for
from app import db
from ..models import User
from flask_login import login_user, current_user


@auth.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        image = request.files['profile_pic']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if confirm_password != password:
            flash('Password does not match', 'danger')
            return redirect(url_for('auth.register'))

        email = User.query.filter_by(email=email).first()
        if email:
            flash('The email has been registered with an account', 'danger')
            return redirect(url_for('auth.register'))

        user = User.query.filter_by(username=username).first()
        if user:
            flash('The username already exists . please choose another one', 'danger')
            return redirect(url_for('auth.register'))

        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully", 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and password == User.password:
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials. check username or password', 'danger')
            return redirect(url_for('auth.login'))
    return render_template('login.html')


@auth.route('/login_with_email', methods=['GET', 'POST'])
def login_with_email():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        email = User.query.filter_by(email=email).first()

        if email and password == User.password:
            login_user(email)
            flash('Logged in successfully', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials. check email or password')
            return redirect(url_for('auth.login_with_email'))
    return render_template('login_with_email.html')



