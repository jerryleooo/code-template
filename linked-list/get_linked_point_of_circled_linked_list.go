/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    
    fast := head
    slow := head
    
    fastStep := 0
    slowStep := 0
        
    for fast != nil {
        if fast == nil || fast.Next == nil {
            return nil
        }
        fast = fast.Next.Next
        slow = slow.Next
        
        fastStep += 2
        slowStep ++
        
        if fast == slow {
            slow = head
            
            for slow != fast {
                slow = slow.Next
                fast = fast.Next
            }
            
            return slow
        }
    }
    
    return nil
}
