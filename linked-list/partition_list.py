"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here

        if not head:
            return None

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left, right = left_dummy, right_dummy

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
