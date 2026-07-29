def armstrong(num):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

number = int(input("Enter a number: "))
print(armstrong(number))