"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here

        if n <= 0:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        
        for i in range(n):
            if not head:
                return None
            head = head.next
            
        while head:
            head = head.next
            pre = pre.next
            
        pre.next = pre.next.next
        return dummy.next