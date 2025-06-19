class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Process both lists while at least one has digits
        while l1 or l2 or carry:
            # Get values (use 0 if list ended)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with current digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
    
# Test cases
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

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular addition with carry
    l1 = createList([2,4,3])  # 342
    l2 = createList([5,6,4])  # 465
    print("Test Case 1:")
    print("Number 1:", end=" ")
    printList(l1)
    print("Number 2:", end=" ")
    printList(l2)
    result1 = solution.addTwoNumbers(l1, l2)
    print("Result:", end=" ")
    printList(result1)
    
    # Test Case 2: Different length lists
    l3 = createList([9,9])    # 99
    l4 = createList([1])      # 1
    print("\nTest Case 2:")
    print("Number 1:", end=" ")
    printList(l3)
    print("Number 2:", end=" ")
    printList(l4)
    result2 = solution.addTwoNumbers(l3, l4)
    print("Result:", end=" ")
    printList(result2)