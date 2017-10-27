"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list 
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        
        if m >= n or not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        for i in range(1, m):
            if not head:
                return None
            head = head.next
            
        pre_m = head
        m_node = head.next
        n_node = m_node
        post_n = n_node.next
        
        for i in range(m, n):
            if not post_n:
                return None
            
            temp = post_n.next
            post_n.next = n_node
            n_node = post_n
            post_n = temp
            
        m_node.next = post_n
        pre_m.next = n_node
        
        return dummy.next