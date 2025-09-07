from flask import jsonify, request
from models.task import Task, db
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        """
        Listar todas as tarefas
        ---
        tags:
          - Tarefas
        responses:
          200:
            description: Lista de tarefas encontradas
            schema:
              type: array
              items:
                properties:
                  id:
                    type: integer
                  title:
                    type: string
                  description:
                    type: string
                  status:
                    type: string
                  user_id:
                    type: integer
          404:
            description: Nenhuma tarefa encontrada
        """
        tasks = Task.query.all()
        if tasks:
            return jsonify([task.dici() for task in tasks]), 200
        else:
            return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

    @staticmethod
    def create_task():
        """
        Criar uma nova tarefa
        ---
        tags:
          - Tarefas
        parameters:
          - name: title
            in: formData
            type: string
            required: true
            description: Título da tarefa
          - name: description
            in: formData
            type: string
            required: true
            description: Descrição da tarefa
          - name: user_id
            in: formData
            type: integer
            required: true
            description: ID do usuário associado
        responses:
          201:
            description: Tarefa criada com sucesso
          400:
            description: Erro na criação da tarefa
        """
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            user_id = request.form["user_id"]

            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return jsonify(new_task.dici()), 201

    @staticmethod
    def update_task_status(task_id):
        """
        Atualizar o status de uma tarefa
        ---
        tags:
          - Tarefas
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
            description: ID da tarefa a ser atualizada
        responses:
          201:
            description: Status da tarefa atualizado com sucesso
          404:
            description: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if task:
            task.status = "Concluído" if task.status == "Pendente" else "Pendente"
            db.session.commit()

            return jsonify(task.dici()), 201
        return jsonify({'mensagem': 'Tarefa não encontrada'}), 404  

    @staticmethod
    def delete_task(task_id):
        """
        Deletar uma tarefa
        ---
        tags:
          - Tarefas
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
            description: ID da tarefa a ser deletada
        responses:
          200:
            description: Tarefa deletada com sucesso
          404:
            description: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()

            return jsonify({'mensagem': 'Tarefa deletada'}), 200
        return jsonify({'mensagem': 'Tarefa não encontrada'}), 404