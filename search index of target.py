user_input = input("Enter numbers separated by spaces (e.g., 1 2 9 3): ")
arr = [int(x) for x in user_input.split()]
target = int(input("enter the Target: "))
num = -1
for i in range(len(arr)):
    if arr[i]== target:
        num = i
        break
print(num)