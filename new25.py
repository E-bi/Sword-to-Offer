new_s1 = [] #大写的情况
new_s2 = [] #小写的情况
def lowerCase(s):
    while s:
        if len(s) == 1:
            new_s1.append(s.lower())
            new_s2.append(s.upper())
            break
        else:
            up = s[0].upper()
            low = s[0].lower()
            new_s1.append(up+s[1:])
            new_s2.append(low+s[1:])
        lowerCase(s[1:])
