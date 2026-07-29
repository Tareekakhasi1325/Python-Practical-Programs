def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        return "Palindrome Number"
    else:
        return "Not a Palindrome Number"

number = int(input("Enter a number: "))
print(palindrome(number))