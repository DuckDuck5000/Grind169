class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base cases
        if not head or not head.next:
            return head
        
        # Split the list into two halves using slow/fast pointer technique
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list
        second_half = slow.next
        slow.next = None
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # Merge the sorted halves
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # Attach remaining nodes
        curr.next = l1 if l1 else l2
        return dummy.next

# Helper functions for testing
def createList(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular list
    head1 = createList([4,2,1,3])
    print("Test Case 1:")
    print("Original:", end=" ")
    printList(head1)
    result1 = solution.sortList(head1)
    print("Sorted:", end=" ")
    printList(result1)
    
    # Test Case 2: List with duplicates
    head2 = createList([-1,5,3,4,0,3])
    print("\nTest Case 2:")
    print("Original:", end=" ")
    printList(head2)
    result2 = solution.sortList(head2)
    print("Sorted:", end=" ")
    printList(result2)