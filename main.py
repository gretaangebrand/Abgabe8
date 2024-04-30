#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET all persons
@app.route('/person/', methods=['GET'])
def get_persons():
    with open('data.json', 'r') as f:
        data = f.read()
        return data


# POST (create a new person)
@app.route('/person/', methods=['POST'])
def create_person():
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

# GET a person by name
@app.route('/person/<name>', methods=['GET'])
def get_person(name):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})
    
# PUT (update a person)
@app.route('/person/<name>', methods=['PUT'])

def update_person(name):
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['name'] == name:
                records[i] = record
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                return jsonify(record)
        return jsonify({'error': 'data not found'})

# DELETE a person
@app.route('/person/<name>', methods=['DELETE'])

def delete_person(name):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['name'] == name:
                record = records.pop(i)
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                record["deleted"] = "True"
                return jsonify(record)
        return jsonify({'error': 'data not found'})


app.run(debug=True)