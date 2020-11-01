n, m, x, y = map(int, input().split())
d_size = list(map(int, input().split()))
a_size = list(map(int, input().split()))

results = []
for i in range(m):
    print("i = ", i)
    for j in range(n):
        print("j = ", j)
        if d_size[j] - x == a_size[i] or d_size[j] + y == a_size[i] or d_size[j] == a_size[i]:
            results.append([i+1, j+1])
            d_size[j] = "PICKLED"
            a_size[i] = "PICKLED"
            print(results)
            break
