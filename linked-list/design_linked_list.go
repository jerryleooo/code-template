package main

type MyLinkedList struct {
	data int
	next *MyLinkedList
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	head := MyLinkedList{0, nil}
	return head
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	cur := this
	for i := 0; i < index; i++ {
		if cur == nil {
			return -1
		}
		cur = cur.next
	}
	if cur != nil && cur.next != nil {
		return cur.next.data
	} else {
		return -1
	}
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	this.next = &MyLinkedList{data: val, next: this.next}
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	cur := this
	for cur.next != nil {
		cur = cur.next
	}
	cur.next = &MyLinkedList{val, nil}
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	cur := this

	canInsert := true
	for i := 0; i < index; i++ {
		if cur == nil {
			canInsert = false
			break
		}
		cur = cur.next
	}

	if canInsert && cur != nil {
		addedNode := MyLinkedList{val, cur.next}
		cur.next = &addedNode
	}
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	cur := this
	canDelete := true

	for i := 0; i < index; i++ {
		if cur == nil {
			canDelete = false
			break
		}
		cur = cur.next
	}

	if canDelete {
		if cur.next != nil {
			cur.next = cur.next.next
		} else {
			cur.next = nil
		}
	}
}
