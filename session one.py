#[10,20,30,40,50]
#[50,10,20,30,40]   n-1 ->number of rotation to the right
#[40,50,10,20,30]   n-2
# wt the output if n=156

arr = [10,20,30,40,50]
num = 146
lenar = len(arr)
num = num % lenar

for x in range(num):
    last = arr[-1]
    for i in range(lenar-1,-1,-1):
        arr[i] = arr[i-1]
    arr[0] = last
print(arr)



