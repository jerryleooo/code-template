"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        
        if not head or not head.next:
            return False
        
        fast = head.next
        slow = head
        
        while fast != slow:
            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next
            
        return True