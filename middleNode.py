# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count the nodes through one loop
        # Traverse up to half of the count
        # Return what has yet to be traversed
        
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        
        ans = head
        for i in range(math.floor(count/2)):
            ans = ans.next
        
        return ans
            
