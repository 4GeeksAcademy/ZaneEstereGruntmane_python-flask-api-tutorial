from flask import Flask
app = Flask(__name__)
from flask import Flask, jsonify


todos [  { "label": "My first task", "done": False },
         { "label": "My second task", "done": False } 
    ]


@app.route('/myroute', methods=['GET'])
def hello_world(): 
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello():
    return '<h1>Hello!</h1>'



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)