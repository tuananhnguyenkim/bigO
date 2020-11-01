n, k = map(int, input().split())
arr = list(map(int, input().split()))

unique = 0
j = 0
result = {}
for i in range(n):
    if arr[i] not in result:
        unique += 1
        result[arr[i]] = 0
    result[arr[i]] += 1
    while unique == k:
        result[arr[j]] -= 1
        if result[arr[j]] == 0:
            print(j+1 , i+1)
            exit()
        j += 1
print(-1, -1)