lst = [10, 20, 30]

print("Original:", lst)

lst.append(40)
print("append():", lst)

lst.insert(1, 15)
print("insert():", lst)

lst.extend([50, 60])
print("extend():", lst)

print("len():", len(lst))
print("count():", lst.count(20))
print("index():", lst.index(30))

lst.remove(15)
print("remove():", lst)

lst.pop()
print("pop():", lst)

lst.reverse()
print("reverse():", lst)

lst.sort()
print("sort():", lst)

copy_list = lst.copy()
print("copy():", copy_list)

lst.clear()
print("clear():", lst)