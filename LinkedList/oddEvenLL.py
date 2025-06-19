class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Handle empty list or single node
        if not head or not head.next:
            return head
        
        odd = head           # First node
        even = head.next     # Second node
        evenHead = even      # Save the head of even list
        
        # Process nodes in pairs
        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            odd = odd.next
            
            # Connect even nodes
            even.next = odd.next
            even = even.next
        
        # Connect odd list with even list
        odd.next = evenHead
        
        return head

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
    
    # Test Case 1: List with odd length
    head1 = create_linked_list([1,2,3,4,5])
    print("Test Case 1:")
    print("Original:", end=" ")
    print_list(head1)
    result1 = solution.oddEvenList(head1)
    print("After reordering:", end=" ")
    print_list(result1)
    
    # Test Case 2: List with even length
    head2 = create_linked_list([1,2,3,4,6,8])
    print("\nTest Case 2:")
    print("Original:", end=" ")
    print_list(head2)
    result2 = solution.oddEvenList(head2)
    print("After reordering:", end=" ")
    print_list(result2)