"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# Merge Sort

class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        
        
        def find_middle(head):
            slow = head
            fast = head.next
        
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                
            return slow
            
        def merge(head1, head2):
            dummy = ListNode(0)
            tail = dummy
            
            while head1 and head2:
                if head1.val < head2.val:
                    tail.next = head1
                    head1 = head1.next
                else:
                    tail.next = head2
                    head2 = head2.next
                    
                tail = tail.next
                
            if head1:
                tail.next = head1
            else:
                tail.next = head2
                
            return dummy.next
            
        if not head or not head.next:
            return head
            
        mid = find_middle(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        
        return merge(left, right)


# Quick Sort 1
class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        
        def find_middle(head):
            slow = head
            fast = head.next
        
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                
            return slow
            
        def concat(left, middle, right):
            dummy = ListNode(0)
            tail = dummy
            
            tail.next = left
            tail = get_tail(tail)
            
            tail.next = middle
            tail = get_tail(tail)
            
            tail.next = right
            tail = get_tail(tail)
            
            return dummy.next
            
        def get_tail(head):
            if not head:
                return None
                
            while head.next:
                head = head.next

            return head
        
        if not head or not head.next:
            return head
            
        mid = find_middle(head)

        left_dummy = ListNode(0)
        left_tail = left_dummy
        
        right_dummy = ListNode(0)
        right_tail = right_dummy
        
        middle_dummy = ListNode(0)
        middle_tail = middle_dummy
        
        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = left_tail.next
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = right_tail.next
            else:
                middle_tail.next = head
                middle_tail = head
                
            head = head.next
            
        left_tail.next = None
        middle_tail.next = None
        right_tail.next = None
        
        left = self.sortList(left_dummy.next)
        right = self.sortList(right_dummy.next)
        
        return concat(left, middle_dummy.next, right)
        
        