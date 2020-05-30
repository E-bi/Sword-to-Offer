#桶排序
#找到列表中最大的元素
#创建全部位0的列表作为桶，桶的大小位最大元素的大小
#把列表中的元素放入桶中，即对应元素+1
#然后再将其从桶中取出
#时间复杂度：O(N+C)，其中C=N*(logN-logM) 
def bucketSort(alist):
    maxNum = max(alist)
    bucket = [0 for i in range(maxNum+1)] 
    for num in alist:
        bucket[num] += 1
    sort_num = [] #储存排序好的元素
    for i in range(maxNum+1):
        if bucket[i]: #如果元素不为0
            for item in range(bucket[i]):
                sort_num.append(i)
    return sort_num


test = [1,3,2,5,4,3,2,5,7,5,3]
print(bucketSort(test))

