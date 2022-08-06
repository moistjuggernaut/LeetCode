from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for idx_outer, first in enumerate(nums):
    #         for idx_inner, second in enumerate(nums[idx_outer + 1:]):
    #             if target == first + second:
    #                 return [idx_outer, idx_inner + idx_outer + 1]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, num in enumerate(nums):
            if target - num in values:
                return [values[target-num], idx]
            else:
                values[num] = idx


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
print(test.twoSum([3, 2, 4], 6))
print(test.twoSum([3, 3], 6))
print(test.twoSum([3, 2, 4], 6))
