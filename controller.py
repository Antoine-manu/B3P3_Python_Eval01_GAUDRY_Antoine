from flask import Flask, jsonify, request
import redis
import json
import pickle
from list import ToDoList   
from task import Task   

app = Flask(__name__)
r = redis.Redis()

@app.route('/list/create', methods=['POST'])
def create_list():
    datas = request.json['list']
    list = ToDoList( datas["name"])
    RedisList = pickle.dumps(list)
    r.lpush('list', RedisList)
    return jsonify({
        'result': "Success",
        "datas" : datas
    })

@app.route('/lists', methods=['GET'])
def get_lists():
    if(r.exists('list')) :
        RedisLists = r.lrange('list', 0, -1)
        lists = pickle.loads(RedisLists)
        return jsonify({
            "Listes" : lists
        })  
    else :
        return jsonify({
            "error" : "error"
        })  


@app.route('/lists/<int:id>', methods=['GET'])
def get_list(id):
    RedisLists = r.lrange('list', 0, -1)
    lists = pickle.loads(RedisLists)
    for list in lists:
        if list['id'] == id:
            return jsonify({'list': list})
    return jsonify({'error': 'Liste non trouvé'})


@app.route('/sensors/<int:id>', methods=['PUT'])
def update_list(id):
    lists = ToDoList( datas["name"])
    RedisList = pickle.dumps(list)
    for list in lists:
        if list['id'] == id:
            updated_list = request.json
            list = ToDoList(updated_list['name'])
            r.lset('list', lists.index(list), json.dumps(updated_list))
            return jsonify({'result': 'success'})
    return jsonify({'error': 'Liste non trouvée'})


@app.route('/sensors/<int:id>', methods=['DELETE'])
def remove_list(id):
    lists = ToDoList( datas["name"])
    RedisList = pickle.dumps(list)
    for list in lists:
        if list['id'] == id:
            r.lrem('list', 0, json.dumps(list))
            return jsonify({'result': 'success'})
    return jsonify({'error': 'Liste non trouvée'})





@app.route('/task/create', methods=['POST'])
def create_list():
    datas = request.json['task']
    task = Task( datas["name"])
    Redistask = pickle.dumps(task)
    r.lpush('task', Redistask)
    return jsonify({
        'result': "Success",
        "datas" : datas
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    if(r.exists('task')) :
        Redistasks = r.lrange('task', 0, -1)
        tasks = pickle.loads(Redistasks)
        return jsonify({
            "taskes" : tasks
        })  
    else :
        return jsonify({
            "error" : "error"
        })  


@app.route('/task/<int:id>', methods=['GET'])
def get_task(id):
    Redistasks = r.lrange('task', 0, -1)
    tasks = pickle.loads(Redistasks)
    for task in tasks:
        if task['id'] == id:
            return jsonify({'task': task})
    return jsonify({'error': 'Task non trouvé'})


@app.route('/sensors/<int:id>', methods=['DELETE'])
def remove_task(id):
    tasks = Task( datas["name"])
    Redistask = pickle.dumps(task)
    for task in tasks:
        if task['id'] == id:
            r.lrem('task', 0, json.dumps(task))
            return jsonify({'result': 'success'})
    return jsonify({'error': 'task non trouvée'})

if __name__ == '__main__':
    app.run(debug=True)
