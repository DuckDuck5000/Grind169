class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for lis in lists:
            while lis:
                heappush(heap, lis.val)
                lis = lis.next
        
        dum = ListNode(-1)
        sent = dum
        
        while heap:
            dum.next = ListNode(heappop(heap))
            dum = dum.next
        return sent.next