from flask import jsonify, request
from models.task import Task, db
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        if tasks:
            return jsonify([task.dici() for task in tasks]), 200
        else:
            return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

    @staticmethod
    def create_task():
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            user_id = request.form["user_id"]

            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return jsonify(new_task), 201

    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get(task_id)
        if task:
            task.status = "Concluído" if task.status == "Pendente" else "Pendente"
            db.session.commit()

            return jsonify(task), 201
        return jsonify({'mensagem': 'Tarefa não encontrada'}), 404  

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()

            return jsonify({'mensagem': 'Tarefa deletada'}), 200
        return jsonify({'mensagem': 'Tarefa não encontrada'}), 404