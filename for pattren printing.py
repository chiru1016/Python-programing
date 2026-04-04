# It's a simple one
# number = [5,2,5,2,2]
# for i in number:
#     print(i*"x")

number = [5,2,5,2,2]
for i in number:
    output = ""
    for j in range(i):
        output += "x"
    print(output)