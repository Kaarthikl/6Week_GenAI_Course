import streamlit as st

# App Title
st.title("📜 History Quiz App")

# Quiz Questions
questions = [
    {
        "question": "Who was the first President of India?",
        "options": [
            "Mahatma Gandhi",
            "Jawaharlal Nehru",
            "Dr. Rajendra Prasad",
            "Sardar Patel"
        ],
        "answer": "Dr. Rajendra Prasad"
    },
    {
        "question": "In which year did India get Independence?",
        "options": [
            "1945",
            "1947",
            "1950",
            "1942"
        ],
        "answer": "1947"
    },
    {
        "question": "Who built the Taj Mahal?",
        "options": [
            "Akbar",
            "Shah Jahan",
            "Aurangzeb",
            "Babur"
        ],
        "answer": "Shah Jahan"
    },
    {
        "question": "Which civilization is one of the oldest in the world?",
        "options": [
            "Roman Civilization",
            "Greek Civilization",
            "Indus Valley Civilization",
            "Chinese Civilization"
        ],
        "answer": "Indus Valley Civilization"
    },
    {
        "question": "Who was known as the Iron Man of India?",
        "options": [
            "Subhash Chandra Bose",
            "Bhagat Singh",
            "Sardar Vallabhbhai Patel",
            "Lal Bahadur Shastri"
        ],
        "answer": "Sardar Vallabhbhai Patel"
    }
]

score = 0

st.subheader("Answer the following questions:")

# Display Questions
user_answers = []

for i, q in enumerate(questions):
    st.write(f"### Q{i+1}. {q['question']}")

    answer = st.radio(
        "Choose your answer:",
        q["options"],
        key=i
    )

    user_answers.append(answer)

# Submit Button
if st.button("Submit Quiz"):

    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎉 Your Score: {score} / {len(questions)}")

    # Performance Message
    if score == len(questions):
        st.balloons()
        st.write("Excellent! You are a History Expert 🏆")

    elif score >= 3:
        st.write("Good Job! 👍")

    else:
        st.write("Keep Learning History 📚")