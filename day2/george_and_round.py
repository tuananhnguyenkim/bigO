n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = n

prepared = list(set(a).intersection(b))
not_prepared = [x for x in b if x not in a]
need_prepare = [x for x in a if x not in b]

for i in range(len(need_prepare)):
    for j in range(len(not_prepared)):
        if not_prepared[j] > need_prepare[i]:
            count -= 1
            not_prepared[j] = 0
            need_prepare[i] = 999999999999

count -= len(prepared)
print(count)

