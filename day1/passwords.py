n, k = map(int, input().split())

list_pass = []
for _ in range(n):
    list_pass.append(input())

output = input()

list_pass = sorted(list_pass)


best_case, worse_case = 0


for i in range(len(list_pass)):
    if list_pass[i] == list_pass[-1]:
        best_case = i

