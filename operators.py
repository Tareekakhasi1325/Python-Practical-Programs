a = 10
b = 3

print("Arithmetic")
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\nRelational")
print(a > b)
print(a == b)

print("\nAssignment")
c = a
print(c)

print("\nLogical")
print(a > 5 and b < 5)

print("\nBitwise")
print(a & b)
print(a | b)

print("\nTernary")
result = "Greater" if a > b else "Smaller"
print(result)