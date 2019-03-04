/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    
    var nodes = make([]*ListNode, 0)
    var length = 0
    cur := head
    
    for cur != nil {
        nodes = append(nodes, cur)
        cur = cur.Next
        length ++
    }
    
    if length <= 1 {
        return nil
    }
    
    if length == n {
        return head.Next
    }
    
    nodes = append(nodes, nil)
        
    nodes[length - n - 1].Next = nodes[length - n + 1]
    
    return head
}
