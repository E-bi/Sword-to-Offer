class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            count += 1
            n = (n-1)&n
        return count
s = Solution()
print(s.NumberOf1(3))
