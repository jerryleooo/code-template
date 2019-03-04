/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    
    if head == nil {
        return false
    }
    
    fast := head
    slow := head
    
    for fast != nil {
        
        if fast == nil || fast.Next == nil {
            return false
        } else {
            fast = fast.Next.Next
            slow = slow.Next  
        }
        
        if fast == slow {
            return true
        }
        
    }
    
    return false
}
