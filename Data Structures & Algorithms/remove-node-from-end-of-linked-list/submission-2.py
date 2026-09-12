# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0 
        curr = head

        while curr:
            length +=1 
            curr = curr.next
        
        removeIndex = length - n # from starting 
        curr = head
        if removeIndex == 0 :
            return head.next
        for i in range(length-1):
            if removeIndex == i+1:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head