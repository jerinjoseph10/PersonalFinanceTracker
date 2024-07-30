#Purpose: Define the database models, including the User model.

from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    email = db.Column(db.string(150), unique = True, nullable = False)
    password = db.Column(db.string(150), unique = False, nullable = False)
    incomes = db.relationship("Income", backref='user', lazy=True)
    Expenses = db.relationship('Expense', backref='user', lazy=False)
    savings_goals = db.relationship('SavingsGoal', backref='user', lazy=True)

class Income(db.Model):
    id = db.Column(db.integer, primary_key=True)
    amount = db.Column 

    






