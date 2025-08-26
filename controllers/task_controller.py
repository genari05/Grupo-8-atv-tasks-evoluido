from flask import render_template, request, redirect, url_for
from models.task import Task, db
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        # Busca todas as tarefas e já permite acessar o nome do usuário pelo relacionamento
        tasks = Task.query.all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            user_id = request.form["user_id"]

            # Cria nova tarefa
            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("task_list"))

        # GET → mostra o formulário
        users = User.query.all()
        return render_template("create_task.html", users=users)

    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get(task_id)
        if task:
            # alterna entre Pendente e Concluído
            task.status = "Concluído" if task.status == "Pendente" else "Pendente"
            db.session.commit()

        return redirect(url_for("task_list"))

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()

        return redirect(url_for("task_list"))
