from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8aafbe5e6d6b4e4149442c12f4fe9c32'
# below creat db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:f00007777@db:3306/post_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

from flask_blog1 import routes