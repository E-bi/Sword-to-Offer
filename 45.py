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
s=['3','32','321']
s += ['\n']
Permutation(s,0)
print(min(tar))

