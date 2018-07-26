# 旋转数组的最小数字
import math


def minNum(nums):
    len_nums = len(nums)
    if len_nums == 1:
        return 0
    elif len_nums == 0:
        return -1
    else:
        left = 0
        right = len_nums-1
        while True:
            mid = math.floor((right+left)/2)
            # 如果出现都相等的情况
            if nums[right] == nums[left]:
                return FindByOrder(nums)
            if nums[left] < nums[right]:
                return 0
            else:
                # 如果中间的元素大于左边的
                if nums[mid] >= nums[left]:
                    left = mid
                    if nums[left+1] <= nums[left]:
                       return left+1
                # 如果中间的元素小于右边的
                if nums[mid] <= nums[right]:
                    right = mid
                    if nums[right-1] > nums[right]:
                        return mid


def FindByOrder(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

nums = [1, 2, 3, 4, 5, 6, 7]
mi = minNum(nums)
if mi == -1:
    print('False')
else:
    print(nums[mi])
