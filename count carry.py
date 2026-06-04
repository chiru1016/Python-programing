#  1 1 1   ------>3 output
#  8 9 6 8
#    6 5 6  (+)
#  9 6 2 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
carry = 0
count = 0
while a > 0 or b > 0:
    digit1 = a % 10
    digit2 = b % 10
    total = digit1 + digit2 + carry
    if total >= 10:
        count += 1
        carry = 1
    else:
        carry = 0
    a = a // 10
    b = b // 10
print(count)