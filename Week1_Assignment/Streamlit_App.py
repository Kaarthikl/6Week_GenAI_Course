import streamlit as st
import requests
import pandas as pd

# Flask API Base URL
API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="History Quiz Admin", layout="wide")

st.title("📜 History Quiz App with CRUD API")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "View Questions",
        "Add Question",
        "Update Question",
        "Delete Question",
        "Take Quiz"
    ]
)

# -------------------------------
# VIEW QUESTIONS
# -------------------------------
if menu == "View Questions":

    st.header("📋 All Quiz Questions")

    response = requests.get(f"{API_URL}/questions")

    if response.status_code == 200:

        data = response.json()

        if len(data) > 0:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No questions available")

    else:
        st.error("Failed to fetch questions")


# -------------------------------
# ADD QUESTION
# -------------------------------
elif menu == "Add Question":

    st.header("➕ Add New Question")

    question = st.text_input("Enter Question")

    option1 = st.text_input("Option 1")
    option2 = st.text_input("Option 2")
    option3 = st.text_input("Option 3")
    option4 = st.text_input("Option 4")

    answer = st.selectbox(
        "Select Correct Answer",
        [option1, option2, option3, option4]
    )

    if st.button("Add Question"):

        payload = {
            "question": question,
            "options": [
                option1,
                option2,
                option3,
                option4
            ],
            "answer": answer
        }

        response = requests.post(
            f"{API_URL}/questions",
            json=payload
        )

        if response.status_code == 201:
            st.success("Question added successfully")
        else:
            st.error("Failed to add question")


# -------------------------------
# UPDATE QUESTION
# -------------------------------
elif menu == "Update Question":

    st.header("✏️ Update Question")

    question_id = st.number_input(
        "Enter Question ID",
        min_value=1,
        step=1
    )

    question = st.text_input("New Question")

    option1 = st.text_input("New Option 1")
    option2 = st.text_input("New Option 2")
    option3 = st.text_input("New Option 3")
    option4 = st.text_input("New Option 4")

    answer = st.selectbox(
        "Correct Answer",
        [option1, option2, option3, option4]
    )

    if st.button("Update Question"):

        payload = {
            "question": question,
            "options": [
                option1,
                option2,
                option3,
                option4
            ],
            "answer": answer
        }

        response = requests.put(
            f"{API_URL}/questions/{question_id}",
            json=payload
        )

        if response.status_code == 200:
            st.success("Question updated successfully")
        else:
            st.error("Question not found")


# -------------------------------
# DELETE QUESTION
# -------------------------------
elif menu == "Delete Question":

    st.header("🗑️ Delete Question")

    question_id = st.number_input(
        "Enter Question ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Question"):

        response = requests.delete(
            f"{API_URL}/questions/{question_id}"
        )

        if response.status_code == 200:
            st.success("Question deleted successfully")
        else:
            st.error("Question not found")


# -------------------------------
# TAKE QUIZ
# -------------------------------
elif menu == "Take Quiz":

    st.header("🎯 Take History Quiz")

    response = requests.get(f"{API_URL}/questions")

    if response.status_code == 200:

        questions = response.json()

        if len(questions) == 0:
            st.warning("No quiz questions available")

        else:

            score = 0
            user_answers = []

            for q in questions:

                st.write(f"### {q['id']}. {q['question']}")

                answer = st.radio(
                    "Choose your answer",
                    q["options"],
                    key=q["id"]
                )

                user_answers.append({
                    "selected": answer,
                    "correct": q["answer"]
                })

            if st.button("Submit Quiz"):

                for ans in user_answers:
                    if ans["selected"] == ans["correct"]:
                        score += 1

                st.success(
                    f"🎉 Your Score: {score} / {len(questions)}"
                )

                if score == len(questions):
                    st.balloons()
                    st.write("🏆 Excellent Performance!")

                elif score >= 3:
                    st.write("👍 Good Job!")

                else:
                    st.write("📚 Keep Practicing!")

    else:
        st.error("Unable to load quiz")