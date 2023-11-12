from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15))


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.Text())
    date = db.Column(db.DateTime(), default = datetime.utcnow)

    def __repr__(self):
        return f'post if: {self.id}, its title: {self.title}, date: {self.date}'


@app.route("/")
def index():

    return render_template('index.html')


@app.route("/brain_info/")
def info():
    return render_template('brain_info.html')



with app.app_context():
    db.create_all()

app.run(debug=True, port=5000)