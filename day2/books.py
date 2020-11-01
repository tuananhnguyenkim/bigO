n, t = map(int, input().split())
arr = list(map(int, input().split()))
j = 0
results = []
for i in range(n):
    result = t - arr[i]
    print(i, result)
    if result > 0:
        results.append(result)
        t = result
    elif result == 0:
        results.append(result)
        break
    else:
        result += arr[i] + arr[0]
        results.pop(0)
        j += 1
        i = j

print(len(results))

#print(sum(arr))
#print(len(arr))


