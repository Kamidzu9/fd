def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

print(divide(4, 2)) # 2.0
print(divide(4, 0)) # AssertionError: Cannot divide by zero