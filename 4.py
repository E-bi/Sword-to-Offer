#!/usr/bin/env python
'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排列，
每一列都按照从上倒下递增的顺序排列。请完成一个函数，
输入这样的一个二位数组和一个整数，判断数组中是否含有该整数。
'''
def Find(tar,s):
    len_mat = len(s)
    R = 0 #行
    C = len_mat-1 #列
    RigTop = s[R][C]
    if RigTop == tar:
        return True
    while RigTop != tar:
        if RigTop > tar:
            C -= 1
            if C < 0:
                return False
            RigTop = s[R][C]
        if RigTop < tar:
            R += 1
            if R >= len_mat:
                return False
            RigTop = s[R][C]
        if RigTop == tar:
            return True
tar = 5
s = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(Find(tar,s))
