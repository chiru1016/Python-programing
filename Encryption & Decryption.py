# SBIVM
# Enc = 1
# Dec = -1
# RAHUL

text = input("Enter text: ")
key = int(input("Enter key: "))   # 1 for encryption, -1 for decryption
ans = ""
for ch in text:
    if ch.isupper():
        ans += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif ch.islower():
        ans += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
        ans += ch
print(ans)