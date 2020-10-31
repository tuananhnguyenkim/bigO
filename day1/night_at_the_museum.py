name = input()
current_point = 'a'
next_point = ''
step = 0
# ASCII alpha lower 97-122
for i in range(len(name)):
    next_point = name[i]
    current_value = ord(current_point)
    next_value = ord(next_point)

    if abs(next_value - current_value) > 13:
        add_value = 26 - (abs(next_value - current_value))
        step += add_value
        current_point = next_point
    else:
        add_value = abs(next_value - current_value)
        step += add_value
        current_point = next_point

print(step)

