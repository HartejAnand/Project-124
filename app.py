from flask import Flask, jsonify, request
app=Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'T-rex',
        'description': u'Tyrant Lizard', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Triceritops',
        'description': u'Three horned face', 
        'done': False
    },
    {
        'id': 3,
        'name': u'pachycephalosaurus ',
        'description': u'Thik-headed lizard', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
        'done': False
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)