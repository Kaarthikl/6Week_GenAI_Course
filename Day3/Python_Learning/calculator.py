# Basic Calculator using list and conditions

numbers = []
operators = []

# Taking input
num1 = int(input("Enter first number: "))
numbers.append(num1)

op = input("Enter operator (+, -, *, /): ")
operators.append(op)

num2 = int(input("Enter second number: "))
numbers.append(num2)

# Conditions
if operators[0] == "+":
    result = numbers[0] + numbers[1]

elif operators[0] == "-":
    result = numbers[0] - numbers[1]

elif operators[0] == "*":
    result = numbers[0] * numbers[1]

elif operators[0] == "/":
    if numbers[1] != 0:
        result = numbers[0] / numbers[1]
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"

# Output
print("Result:", result)