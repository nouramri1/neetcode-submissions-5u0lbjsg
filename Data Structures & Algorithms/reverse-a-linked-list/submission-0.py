# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None 
        while current:
            #store my next node 
            nxt = current.next
            # point to the prevuious node 
        
            current.next = prev
            # reset the pointers 
            prev = current
            current = nxt

        return prev

            
            

        
        