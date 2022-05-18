# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.next)
        print(l1.val)
            




l1 = [2,4,3]
l2 = [5,6,4]
l3 = [0]

l5 = [9,9,9,9,9,9,9]
l6 = [9,9,9,9]
test1 = Solution()
test1.addTwoNumbers(l1,l2)