from flask_sqlalchemy import SQLAlchemy
from models.user import User, db  # importa db já criado no user

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(100), nullable=False, default="Pendente")

    # chave estrangeira -> users.id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"
