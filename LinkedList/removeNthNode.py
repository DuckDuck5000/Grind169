class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = dummy
        slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next

# Test code
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Remove 2nd node from end
    head1 = create_linked_list([1,2,3,4,5])
    print("Test Case 1:")
    print("Original:", end=" ")
    print_list(head1)
    result1 = solution.removeNthFromEnd(head1, 2)
    print("After removing 2nd node from end:", end=" ")
    print_list(result1)
    
    # Test Case 2: Remove head node
    head2 = create_linked_list([1])
    print("\nTest Case 2:")
    print("Original:", end=" ")
    print_list(head2)
    result2 = solution.removeNthFromEnd(head2, 1)
    print("After removing 1st node from end:", end=" ")
    print_list(result2)