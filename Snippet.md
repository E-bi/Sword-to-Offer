### 给定一个没有重复数字的序列，返回其所有可能的全排列。
```py
from typing import List
import itertools
def permute(nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
nums = [1,2,3]
permute(nums)
```
