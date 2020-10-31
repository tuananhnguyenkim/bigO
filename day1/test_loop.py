s = 'yzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
s = 'azzz'
for i in range(len(s) - 1 , 0, -1):
    if s[i] == 'z':
        s = s[:i] + 'a' + s[i+1:]
        j = i - 1
        if s[j] != 'z':
            s = s[:j] + chr(ord(s[j]) + 1) + s[j+1:]

print(s)
if s < 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz':
    print('True')
else:
    print('False')