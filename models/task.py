from flask_sqlalchemy import SQLAlchemy
from models.user import User, db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(100), nullable=False, default="Pendente")

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __init__(self, title, description, status, user_id):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id

    def dici(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }
