# Defines the routes (endpoints) for your application.

from flask import Blueprint, render_template, url_for, flash, redirect
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

# Create a new Blueprint instance for handling routes
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Render the index.html template when the root URL is accessed
    return render_template('index.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Corrected to User.query.filter_by
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username or password', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/dashboard')  # Corrected to @bp.route
@login_required
def dashboard():
    return render_template('dashboard.html')
