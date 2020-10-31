
n = int(input())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

(l, r) = list(zip(*segments))
max_value = max(r)
min_value = min(l)
result = -1
if [min_value, max_value] in segments:
    result = segments.index([min_value, max_value]) + 1
print(result)
