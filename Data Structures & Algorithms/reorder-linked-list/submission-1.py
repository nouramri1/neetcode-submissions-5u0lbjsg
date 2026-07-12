# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the linked list 
        slow, fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # second half is the slow pointer.next
        second = slow.next 
        slow.next = None 
        # reverse the second part of the linked list 
        current = second 
        prev = None 
        while current:
            nxt = current.next 
            current.next = prev
            prev = current
            current = nxt 
        # start of the second half is prev 
        # we gotta merge the lists
        first, second = head, prev
        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2 


        

        