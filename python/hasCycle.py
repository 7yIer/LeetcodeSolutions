# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize a fast and slower pointer
        # Traverse the list until
        # If the fast and slow pointer are ever equal, it must contain a cycle
        # Else we reach none and we return false
        
        slow = fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
        
