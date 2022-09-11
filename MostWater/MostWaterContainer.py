from cgitb import reset
import enum
from typing import List


class Solution:
    # Niet perse een betere oplossing dan de vorige commit
    def maxArea(Self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_left = height[lp]
        max_right = height[rp]
        result = min(height[lp], height[rp]) * (rp-lp)
        if len(height) == 2:
            return min(height)
        while lp < rp:
            if max_left < max_right:
                if max_left < height[lp]:
                    max_left = height[lp]
                    result = max(result, min(height[lp], height[rp]) * (rp-lp))
                else:
                    lp += 1
            else:
                if max_right < height[rp]:
                    max_right = height[rp]
                    result = max(result, min(height[lp], height[rp]) * (rp-lp))
                else:
                    rp -= 1
        return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]
height = [4, 3, 2, 1, 4]
sln = Solution()
sln.maxArea(height)
