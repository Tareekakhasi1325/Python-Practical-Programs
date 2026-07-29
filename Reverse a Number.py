def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

number = int(input("Enter a number: "))
print("Reverse Number:", reverse_number(number))