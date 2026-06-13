number = [1,2,2,5,7,3,9,4,4,2,6,7,]
# new = []
# for i in number:
#     if i not in new:
#         new.append(i)
# # new.sort()
# print(new)

# 2nd method
i = 0
j = 1
while i<len(number) and j < len(number):
    if number[i] == number[j]:
        number.remove(number[i])
        j += 1
    else:
        i += 1
print(number)