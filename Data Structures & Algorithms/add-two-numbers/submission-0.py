# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            prev, current = None, head
            while current:
                nxt = current.next
                current.next = prev
                prev = current 
                current = nxt 
            return prev
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        # put them in an integer 
        def put_them_in_a_int (head):
            s = ''
            current = head 
            while current:
                s += str(current.val)
                current = current.next
            return s
        s1 = int(put_them_in_a_int(l1))
        s2 = int (put_them_in_a_int(l2))
        res = s1 + s2 

        dummy = ListNode()
        current = dummy 
        for digit in (str(res)):
            current.next = ListNode(int(digit))
            current = current.next
        head = reverse_list(dummy.next)
        return head

        

    
        