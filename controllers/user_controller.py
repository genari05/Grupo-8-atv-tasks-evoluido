from flask import jsonify, request
from models.user import User, db

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        if users:
            return jsonify([user.dici() for user in users]), 200
        else:
            return jsonify({'mensagem': 'User não encontrado'}), 404

    @staticmethod
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.dici()), 201