from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = datetime.now().year

turn60 = current_year + (60 - age)

print(name, "will turn 60 in", turn60)