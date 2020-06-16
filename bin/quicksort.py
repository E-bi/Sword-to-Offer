#快速排序
def quickSort(alist):
    if len(alist) < 2:
        return alist
    mid = alist[0]
    smaller = [item for item in alist if item < mid]
    bigger = [item for item in alist if item > mid]
    equa = [item for item in alist if item == mid]
    return quickSort(smaller) + equa + quickSort(bigger)


# test = [1,3,2,5,4,3,2,5,7,5,3]
test = [7,6,5,4,3,2,1]
print(quickSort(test))
