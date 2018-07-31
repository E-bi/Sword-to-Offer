def bubbleSort(nums):
    for index in range(len(nums)-1,0,-1):
        for indexs in range(index):
            if nums[indexs]>nums[indexs+1]:
                nums[indexs],nums[indexs+1] = nums[indexs+1],nums[indexs]
    return nums

nums = [4,2,1,5,3]
print(bubbleSort(nums))
