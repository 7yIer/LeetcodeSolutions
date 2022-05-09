# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new dummy node that will be the start
        # Traverse both list1 and list2 until they are none
        # Compare them and add respectievly
        
        root = dummy = ListNode()
        
        while list1 is not None or list2 is not None:
            if list1 is None:
                dummy.next = ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
            elif list2 is None:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next
            elif list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
        
        return root.next
                
