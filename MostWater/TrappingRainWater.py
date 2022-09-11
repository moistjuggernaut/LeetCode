from typing import List

# TIP: denk meer aan de vorige oefening waarbij je met 2 pointers werkt en steeds diegen opschuift die kleiner is, onderstaande oplossing is te omslachtig of gaat niet meer werken denk ik


class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, 1
        rocks = 0
        basin = []
        limit = 0
        while j < len(height):
            if height[i] > limit:
                limit = height[i]
            if limit <= height[j]:
                basin.append(min(height[i], height[j]) * (j-i-1) - rocks)
                i = j
                rocks = 0
                if limit > max(height[i+1:]):
                    limit = max(height[i+1:])

            else:
                rocks += height[j]
            j += 1
        return sum(basin)


sln = Solution()
# sln.trap([4, 2, 0, 3, 2, 5])
sln.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
