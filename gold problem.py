arr = [9, 2, 3, 1, 7, 11, 8]
n = len(arr)
maxProfit = 0
minValue = arr[0]
for i in range(n):
    if arr[i] < minValue:
        minValue = arr[i]
    profit = arr[i] - minValue
    if profit > maxProfit:
        maxProfit = profit
print(maxProfit)

