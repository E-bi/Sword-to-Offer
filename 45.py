tar = []
def Permutation(s,start):
    if not s:
        return
    if s[start] == '\n':
        global tar
        tar.append(int(''.join(s[:start])))
    else:
        for j in range(start,len(s)-1):
            s[j], s[start] = s[start], s[j]
            Permutation(s,start+1)
            s[j], s[start] = s[j], s[start]
def MinNum(s):
    s += ['\n']
    Permutation(s,0op)
    return min(tar)
s=['3','32','321']
print(MinNum(s))


