# =======================
for i in range(1, 6):
    print(str(i) * i)
# ========================
for i in range(1, 6):
    for j in range(i):
        print(chr(64 + i), end=" ")
    print()
# ========================
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
# =======================
for i in range(5, 0, -1):
    print("*" * i)
# =======================
