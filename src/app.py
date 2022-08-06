from flask import Flask
import flask #sin esta línea no funciona
app = Flask(__name__)
from flask import request
import json



todos = [
    {'label': 'Una tarea', 'done': False},
    {'label': 'Otra tarea', 'done': False}
    
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return flask.jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return flask.jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return flask.jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)