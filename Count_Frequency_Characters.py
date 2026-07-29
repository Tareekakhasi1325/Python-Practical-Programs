file = open("sample.txt", "r")
text = file.read()
file.close()

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
for key, value in freq.items():
    print(key, ":", value)