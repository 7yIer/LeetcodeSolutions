# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Traverse the linked list
        # If the value is not the target, put it in the array
        # Loop through the array and create a linked list from the values
        
        arr = []
        curr = head
        
        while curr is not None:
            if curr.val != val:
                arr.append(curr.val)
            curr = curr.next
        
        root = dummy = ListNode()
        for i in arr:
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return root.next
            
        
