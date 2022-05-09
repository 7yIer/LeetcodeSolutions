# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Loop through the whole linked list
        # Store each value in an array
        # Reverse the array
        # Compare the reversed and non reversed array
        
        vals = []
        curr = head
        
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        
        return vals == vals[::-1]
