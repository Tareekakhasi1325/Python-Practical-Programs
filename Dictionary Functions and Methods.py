student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Rajkot"
}

print(student)

print("Length:", len(student))

print("Get Name:", student.get("Name"))

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

student.update({"Age": 21})
print("Update:", student)

student.pop("City")
print("Pop:", student)

copy_dict = student.copy()
print("Copy:", copy_dict)

student.clear()
print("Clear:", student)