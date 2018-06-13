#!/usr/bin/env python
def matnum(num):
    s = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    for i in range(len(s)):
        if num in s[i]:
            return True
    return False

num = 7
print(matnum(num))
