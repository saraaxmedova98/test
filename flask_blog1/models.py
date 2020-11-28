from flask_blog1 import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"