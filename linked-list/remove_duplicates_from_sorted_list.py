"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here

        if not head:
            return None
            
        node = head
        
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
                
        return head