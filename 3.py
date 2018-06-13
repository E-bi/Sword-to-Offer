# -*- coding:utf-8 -*-
#题目一：找出数组中重复的数字

#方法一：
def findnum1(s):
    len_s = len(s)
    if len_s == 0:
        return False
    elif len_s == 1:
        return ss
    else:
        #s.sort() useless
        for index in range(len_s):
            buff_s = s[index+1:]
            if s[index] in buff_s:
                return s[index]
s = [0,2,3,5,4,5,6,4,3]
s=[]
s=[1]
s=[1,2]
s=[1,1]
num1 = findnum1(s)
print(num1)
