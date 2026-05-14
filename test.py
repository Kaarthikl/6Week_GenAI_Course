print("test")
name = "kaarthik"
print("name")
print(name)


try:
    c = 10/3
    print(c)
except Exception as e:
    print("Cannot divide by zero")
    print("Error:", e)
else:
    print("Division successful")
finally:
    print("This will always execute")