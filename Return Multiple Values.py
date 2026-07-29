def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

x, y, z = calculate(20, 10)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)