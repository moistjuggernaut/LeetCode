from cgitb import reset
import enum
from typing import List


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     result = 0
    #     for i, num in enumerate(height):
    #         for y, inner in enumerate(height):
    #             current = min(num, inner)*(y-i)
    #             if current > result:
    #                 result = current
    #     return result

    def maxArea(Self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            # for speed, min and max functions are bad
            result = max(result, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sln = Solution()
sln.maxArea(height)
