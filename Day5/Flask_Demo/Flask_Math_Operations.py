from flask import Flask, request, jsonify

app = Flask(__name__)

# -----------------------------------
# ADDITION API
# -----------------------------------

@app.route('/add', methods=['GET'])
def add():

    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    result = num1 + num2

    return jsonify({
        "operation": "Addition",
        "num1": num1,
        "num2": num2,
        "result": result
    })

# -----------------------------------
# SUBTRACTION API
# -----------------------------------

@app.route('/subtract', methods=['GET'])
def subtract():

    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    result = num1 - num2

    return jsonify({
        "operation": "Subtraction",
        "num1": num1,
        "num2": num2,
        "result": result
    })

# -----------------------------------
# MULTIPLICATION API
# -----------------------------------

@app.route('/multiply', methods=['GET'])
def multiply():

    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    result = num1 * num2

    return jsonify({
        "operation": "Multiplication",
        "num1": num1,
        "num2": num2,
        "result": result
    })

# -----------------------------------
# DIVISION API
# -----------------------------------

@app.route('/divide', methods=['GET'])
def divide():

    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    if num2 == 0:
        return jsonify({
            "error": "Division by zero is not allowed"
        })

    result = num1 / num2

    return jsonify({
        "operation": "Division",
        "num1": num1,
        "num2": num2,
        "result": result
    })

# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)