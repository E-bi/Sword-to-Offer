# 实现一个二分查找
#输入：一个顺序list
#输出：带查找的元素的位置
def binarySearch(alist,item):
    l = 0 #左边指针
    r = len(alist) - 1 #右边指针
    while l <= r:
        mid  = (l+r)//2 #中间指针
        if alist[mid] == item:
            return mid
        if alist[mid] > item:
            r = mid - 1
        if alist[mid] < item:
            l = mid + 1 
    return -1
    
test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(test, 8))
