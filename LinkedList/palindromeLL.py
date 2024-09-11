class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        left = 0
        right = len(temp)-1
        while left < right:
            if temp[left] != temp[right]: return False
            left += 1
            right -= 1
        return True