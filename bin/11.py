# 旋转数组的最小数字
def FindRotate(s):
    len_s = len(s)
    if len_s <= 0:
        return None
    if len_s == 1:
        return s
    else:
        start = 0
        end = len_s-1
        mid = (start+end)//2
        while True:
            if s[start]> s[mid]:
                end = mid
                mid = (start+end)//2
            else:
                start = mid
                mid = (start+end)//2
            if start == end-1:
                return s[end]
            if s[start] < s[end]:
                return s[0]

nums = [4, 5, 6, 7,1,2,3]
print(FindRotate(nums))
