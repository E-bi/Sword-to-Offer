#!/usr/bin/env python
#用函数库
def changewithspace(s):
    new_s = s.replace(' ','%20')
    return new_s
s="we are happy"
#不用函数库
def ChangeSpace(S):
    buff_s = []
    for char in s:
        if char is not ' ':
            buff_s.append(char)
        if char is ' ':
            buff_s.append('%20')
    return ''.join(buff_s)


print(changewithspace(s))
print(ChangeSpace(s))
    
