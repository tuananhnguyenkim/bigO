num_buttons = int(input())
buttons = input().split()

count = 0
if num_buttons > 1:
    for i in range(num_buttons):
        if int(buttons[i]) == 0:
            count += 1
    if count == 1:
        print("YES")
    else:
        print("NO")
else:
    if int(buttons[0]) == 0:
        print("NO")
    else:
        print("YES")

