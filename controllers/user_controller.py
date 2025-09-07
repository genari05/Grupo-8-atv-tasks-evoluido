from flask import jsonify, request
from models.user import User, db

class UserController:
    @staticmethod
    def index():
        """
        Listar todos os usuários
        ---
        tags:
          - Usuários
        responses:
          200:
            description: Lista de usuários encontrada
            schema:
              type: array
              items:
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  email:
                    type: string
          404:
            description: Nenhum usuário encontrado
        """
        users = User.query.all()
        if users:
            return jsonify([user.dici() for user in users]), 200
        else:
            return jsonify({'mensagem': 'User não encontrado'}), 404

    @staticmethod
    def contact():
        """
        Criar um novo usuário (contato)
        ---
        tags:
          - Usuários
        parameters:
          - name: name
            in: formData
            type: string
            required: true
            description: Nome do usuário
          - name: email
            in: formData
            type: string
            required: true
            description: Email do usuário
        responses:
          201:
            description: Usuário criado com sucesso
            schema:
              properties:
                id:
                  type: integer
                name:
                  type: string
                email:
                  type: string
          400:
            description: Erro na criação do usuário
        """
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.dici()), 201