/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"

func isPalindrome(head *ListNode) bool {
	length := 0
	node := head

	for {
		if node == nil {
			break
		}
		length += 1
		node = node.Next
	}

	slow := head
	fast := head
	stack := make([]int, 0)

	for {
		if fast == nil || fast.Next == nil {
			break
		}
		stack = append(stack, slow.Val)
		fast = fast.Next.Next
		slow = slow.Next
	}

	if length%2 != 0 {
		slow = slow.Next
	}
	var pop int
	for ; slow != nil; slow = slow.Next {
		pop, stack = stack[len(stack)-1], stack[:len(stack)-1]
		if pop != slow.Val {
			return false
		}
	}
	return true
}