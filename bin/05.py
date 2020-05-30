#!/usr/bin/env python
'''
面试题5：替换空格
题目：请实现一个函数，把字符串中的每个空格替换成%20。例如，输入“we are happy”，则输出“we%20are%20happy”。
'''
#用函数库
def ReplaceBlank1(s):
    new_s = s.replace(' ','%20')
    return new_s

#不用函数库
def ReplaceBlank2(s):
    buff_s = []
    for char in s:    
        if char is ' ':
            buff_s.append('%20')
        else:
            buff_s.append(char)
    return ''.join(buff_s)


s="wh    appy"
print(ReplaceBlank1(s))
print(ReplaceBlank2(s))
    
