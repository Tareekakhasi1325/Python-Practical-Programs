# Write into file
f = open("sample.txt", "w")
f.write("Welcome to Python.\n")
f.write("This is File Handling.")
f.close()

# Read from file
f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()