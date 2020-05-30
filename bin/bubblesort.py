#实现冒泡排序
#时间复杂度O(n^2)
def bubbleSort(alist):
    if not alist:
        return None
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    return alist

test = [1,42,4,3,4,2,5,7,4,3,2]
print(bubbleSort(test))


