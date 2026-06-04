# n = 6\
# ARRIVAL : {900,940,950,1100,1500,1800}
# DEPATURE : {910,1200,1120,1130,1900,2000}
# Max Platform Required?
n = 6
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()
i = 0   # arrival pointer
j = 0   # departure pointer
platforms = 0
max_platforms = 0
while i < n and j < n:
    if arr[i] <= dep[j]:
        platforms += 1
        max_platforms = max(max_platforms, platforms)
        i += 1
    else:
        platforms -= 1
        j += 1
print(max_platforms)

