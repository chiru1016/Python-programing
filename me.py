def getMinimumMachines(start, end):
    n = len(start)
    ans = 0

    for i in range(n):
        count = 0

        for j in range(n):
            if start[j] <= start[i] <= end[j]:
                count += 1

        ans = max(ans, count)

    return ans