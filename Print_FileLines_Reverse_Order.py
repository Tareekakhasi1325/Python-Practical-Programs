file = open("sample.txt", "r")
lines = file.readlines()
file.close()

for line in reversed(lines):
    print(line.strip())