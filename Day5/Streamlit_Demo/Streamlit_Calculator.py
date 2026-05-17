import streamlit as st

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("Simple Calculator App")

st.write("Perform basic mathematical operations")

# -----------------------------------
# USER INPUTS
# -----------------------------------

num1 = st.number_input("Enter First Number")

num2 = st.number_input("Enter Second Number")

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# -----------------------------------
# CALCULATION
# -----------------------------------

if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":

        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed")
            st.stop()

    # Display Result
    st.success(f"Result: {result}")