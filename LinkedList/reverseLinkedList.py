class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head
        while curr:
            nextT = curr.next
            curr.next = prev
            prev, curr = curr, nextT
        return prev