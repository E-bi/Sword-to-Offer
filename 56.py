def FindNumsAppearOnce(s):
    s.sort()
    for i in range(0,len(s)-1,2):
        if s[i] != s[i+1]:
            return s[i],s[i+1]




s = [2,4,3,6,3,2,5,5]
print(FindNumsAppearOnce(s))
