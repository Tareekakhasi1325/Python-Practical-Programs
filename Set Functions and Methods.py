A = {10, 20, 30}
B = {30, 40, 50}

A.add(60)
print("add():", A)

A.update([70, 80])
print("update():", A)

C = A.copy()
print("copy():", C)

A.remove(20)
print("remove():", A)

A.discard(100)
print("discard():", A)

print("union():", A.union(B))

print("intersection():", A.intersection(B))

print("difference():", A.difference(B))

A.pop()
print("pop():", A)

A.clear()
print("clear():", A)