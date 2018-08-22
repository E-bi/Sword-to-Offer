#实现插入排序
#平均来说插入排序算法的时间复杂度为O(n^2）
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentValue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentValue
    return alist
test = [7,6,5,2,4,6,8,4,1]
print(insertionSort(test))
