from flask import Flask, jsonify, request

app = Flask(__name__)

# Home Endpoint
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask API Application"
    })

# GET Endpoint
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')

    return jsonify({
        "message": f"Hello, {name}"
    })

# POST Endpoint
@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)

    result = num1 + num2

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": result
    })

# PUT Endpoint
@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    return jsonify({
        "message": f"User {user_id} updated successfully",
        "updated_data": data
    })

# DELETE Endpoint
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    return jsonify({
        "message": f"User {user_id} deleted successfully"
    })

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)