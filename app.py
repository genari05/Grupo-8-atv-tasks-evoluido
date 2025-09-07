import os
from flask import Flask
from flasgger import Swagger
from config import Config # importa as 
from controllers.user_controller import UserController
from controllers.task_controller import TaskController
from models.user import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "info": {
        "title": "API de Tarefas",
        "description": "Documentação da API de Tarefas e Usuários com Swagger UI (Flasgger).",
        "version": "1.0.0"
    },
    "basePath": "/",  # base da API
    "schemes": ["http", "https"]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['POST'])
app.add_url_rule('/tasks', 'task_list', TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks/new', 'create_task', TaskController.create_task, methods=['POST'])
app.add_url_rule('/tasks/update/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['PUT'])
app.add_url_rule('/tasks/delete/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)