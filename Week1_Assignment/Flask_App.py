from flask import Flask, jsonify, request

app = Flask(__name__)

questions = [
    {
        "id": 1,
        "question": "Who was the first President of India?",
        "options": [
            "Mahatma Gandhi",
            "Jawaharlal Nehru",
            "Dr. Rajendra Prasad",
            "Sardar Patel"
        ],
        "answer": "Dr. Rajendra Prasad"
    }
]

# GET ALL QUESTIONS
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

# ADD QUESTION
@app.route('/questions', methods=['POST'])
def add_question():

    data = request.get_json()

    new_question = {
        "id": len(questions) + 1,
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"]
    }

    questions.append(new_question)

    return jsonify({
        "message": "Question added successfully"
    }), 201

# UPDATE QUESTION
@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id):

    data = request.get_json()

    for q in questions:

        if q["id"] == id:

            q["question"] = data["question"]
            q["options"] = data["options"]
            q["answer"] = data["answer"]

            return jsonify({
                "message": "Question updated successfully"
            })

    return jsonify({
        "message": "Question not found"
    }), 404

# DELETE QUESTION
@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):

    global questions

    questions = [q for q in questions if q["id"] != id]

    return jsonify({
        "message": "Question deleted successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)