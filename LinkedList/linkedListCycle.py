class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head

        while fast and fast.next:
            if fast.next == slow: return True
            slow = slow.next
            fast = fast.next.next
        return False