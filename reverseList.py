# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse the linked list
        # Hold on to the previous node
        # Set the curr.next to the previous node
        # Set the previous to curr
        # set curr to the temp saved variable
        
        curr = head
        prev = None
        
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
