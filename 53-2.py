import math
a=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def findele(a):
    left = 0
    right = len(a)
    while left<=right:
        mid_index = math.floor((left+right)/2)
        if a[mid_index] == mid_index:#如果下标和元素值相等则说明目标在右边
            left = mid_index+1      
        else:#如果下标和元素值不相等则说明目标在左边
            right = mid_index-1
        if left-1 == right:
            return right
right = findele(a)
print(right+1)

