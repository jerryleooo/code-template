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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        
        def find_middle(head):
            slow = head
            fast = head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
            
        def reverse(head):
            pre = None
            
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
                
            return pre
            
        def merge(head1, head2):
            i = 0
            dummy = ListNode(0)
            
            while head1 and head2:
                if i % 2 == 0:
                    dummy.next = head1
                    head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                    
                dummy = dummy.next
                i += 1
                
            if head1:
                dummy.next = head1
            else:
                dummy.next = head2
            
        if not head or not head.next:
            return
        
        mid = find_middle(head)
        tail = reverse(mid.next)
        mid.next = None
        
        merge(head, tail)