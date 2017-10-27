"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# Divide & Conquer

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        
        if not lists:
            return None
            
        def helper(start, end):
            if start == end:
                return lists[start]
                
            mid = start + (end - start) / 2
            left = helper(start, mid)
            right = helper(mid + 1, end)
            
            return merge_two_lists(left, right)
            
        def merge_two_lists(L1, L2):
            dummy = ListNode(0)
            tail = dummy
            
            while L1 and L2:
                if L1.val < L2.val:
                    tail.next = L1
                    L1 = L1.next
                else:
                    tail.next = L2
                    L2 = L2.next
                    
                tail = tail.next
                
            if L1:
                tail.next = L1
            else:
                tail.next = L2
                
            return dummy.next
            
        return helper(0, len(lists) - 1)

# Heap

import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        
        if not lists:
            return None
            
        heap = []
        
        for L in lists:
            if L:
                heapq.heappush(heap, (L.val, L))
            
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            _, head = heapq.heappop(heap)
            tail.next = head
            tail = tail.next
            if head.next:
                heapq.heappush(heap, (head.next.val, head.next))
                
        return dummy.next