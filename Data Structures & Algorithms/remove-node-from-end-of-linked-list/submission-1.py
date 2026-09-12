# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        left = dummy
        right = head

        i = n 
        while i != 0 :
            right = right.next
            i -=1
        
        while right :
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next

        # Here i am starting at left = 0 dummy ll 
        # then i am taking right pointer to n steps from starting head 
        # and then we iterate both left and right together until right goes to the other 
        # end such that are left is at now exactly n + 1 from right end and we then 
        # update left.next = left.next.next