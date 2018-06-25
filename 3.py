# -*- coding:utf-8 -*-
def duplicate(s):
    len_s = len(s)
    if len_s == 0:
        return False
    elif len_s == 1:
        return s
    else:
        for index in range(len_s):
            buff = s[index+1:]
            if s[index] in buff:
                return s[index]
s = [0,2,3,5,4,5,6,4,3]
num = duplicate(s)
print(num)
