# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set() # Use a set to store visited TVs
        curr = head

        while curr:
            if curr in seen_nodes: # Checking if we have physically been to this exact node
                return True 
                
            seen_nodes.add(curr)   # Add the actual node object, not curr.val
            curr = curr.next
            
        return False