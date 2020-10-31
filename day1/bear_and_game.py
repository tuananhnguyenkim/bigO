num = int(input())
minutes = list(map(int, input().split()))

def bear_watch_game(minutes):
    value = 0
    if minutes[0] > 15:
        value = 15
        return value
    for i in range(len(minutes) - 1):
        if minutes[i+1] - minutes[i] > 15:
            value = minutes[i] + 15
            return value
    if minutes[-1] + 15 >= 90:
        value = 90
        return value
    else:
        value = minutes[-1] + 15
        return value

result = bear_watch_game(minutes)
print(result)