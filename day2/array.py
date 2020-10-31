import time

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def find_arr(n, k , arr):
    start = time.time()
    unique, point = 0, 0
    result = (-1, -1)
    if len(set(arr)) < k:
        return result
    for i in range(k, n):
        choose_arr = arr[:i]
        unique = len(set(choose_arr))
        while unique == k:
            choose_arr = choose_arr[point:]
            unique = len(set(choose_arr))
            if unique != 3:
                end = time.time()
                print(end - start)
                return (point, i)
            point += 1

    return result



test = find_arr(n, k, arr)
print(test)
"""
unique = 0
i = 0
if len(set(arr)) < k:
    print(-1, -1)
    quit()
for s in range(n):
    result = arr[:s]
    unique = len(set(result))
    while unique == k:
        for i in range(s):
            if len(set(result[i:])) != k:
                print(i, s)
                quit()
print(-1, -1)
"""
