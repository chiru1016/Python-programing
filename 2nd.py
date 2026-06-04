# Excel Pattern
## 1-> A
## 2-> B
## 26-> Z
## 27-> AA
## 28-> AB
## 52-> AZ
## 53-> BA

import string

letters = list(string.ascii_uppercase)
num = int(input("Enter num: "))
ans = ""
while num > 0:
    num = num - 1
    remainder = num % 26
    ans = letters[remainder] + ans
    num = num // 26
print(ans)



