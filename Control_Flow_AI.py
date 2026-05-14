# Control Flow Operations in Python

# 1. IF Condition
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")


# 2. IF-ELSE Condition
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 3. IF-ELIF-ELSE Condition
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. FOR Loop
print("\nFOR Loop Example:")

for i in range(1, 6):
    print(i)


# 5. WHILE Loop
print("\nWHILE Loop Example:")

count = 1

while count <= 5:
    print(count)
    count += 1


# 6. BREAK Statement
print("\nBREAK Example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 7. CONTINUE Statement
print("\nCONTINUE Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)