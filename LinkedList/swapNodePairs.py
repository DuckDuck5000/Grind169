class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Handle empty list or single node
        if not head or not head.next:
            return head
        
        # Create dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers
            prev = first
            head = first.next
        
        return dummy.next

# Helper function to create linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# Helper function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Even number of nodes
    head1 = create_linked_list([1,2,3,4])
    print("Test Case 1:")
    print("Original:", end=" ")
    print_list(head1)
    result1 = solution.swapPairs(head1)
    print("After swapping:", end=" ")
    print_list(result1)
    
    # Test Case 2: Odd number of nodes
    head2 = create_linked_list([1,2,3])
    print("\nTest Case 2:")
    print("Original:", end=" ")
    print_list(head2)
    result2 = solution.swapPairs(head2)
    print("After swapping:", end=" ")
    print_list(result2)