length_array = list(map(int, input().split()))
numbers = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

nA, nB = numbers[0], numbers[1]
chosse_A = arrayA[:nA]
chosse_B = arrayB[-nB:]
def compare(a, b):
    if a[-1] >= b[0]:
        return "NO"
    return "YES"

print(compare(chosse_A, chosse_B))