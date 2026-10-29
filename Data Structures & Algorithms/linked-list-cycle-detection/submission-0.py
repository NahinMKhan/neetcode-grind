# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        curr = head
        vals = {}

        while curr:
            if curr.val in vals:
                return True 
            vals[curr.val] = index
            curr = curr.next
            index += 1
        return False
