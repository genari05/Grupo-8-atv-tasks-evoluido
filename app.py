import os
from flask import Flask
from config import Config # importa as 
from controllers.user_controller import UserController
from controllers.task_controller import TaskController
from models.user import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['POST'])
app.add_url_rule('/tasks', 'task_list', TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks/new', 'create_task', TaskController.create_task, methods=['POST'])
app.add_url_rule('/tasks/update/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['PUT'])
app.add_url_rule('/tasks/delete/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)