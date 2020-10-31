s = input()
t = input()

def generate_new_string(s, t):
    if s > t:
        return "No such string"
    else:
        add_char = chr(ord(s[-1]) + 1)
        if add_char > 'z':
            for i in range(len(s)-1, 0, -1):
                if s[i] == 'z':
                    s = s[:i] + 'a' + s[i+1:]
                    j = i - 1
                    if s[j] != 'z':
                        s = s[:j] + chr(ord(s[j])+1) + s[j+1:]
            value = s
            return value
        value = s[:-1] + add_char
        if value >= t:
            return "No such string"
        else:
            return value

result = generate_new_string(s, t)
print(result)

