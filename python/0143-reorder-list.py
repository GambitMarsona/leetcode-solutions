# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        prev, slow.next = None, None
        while sec:
            nxt = sec.next
            sec.next = prev
            prev = sec
            sec = nxt
        
        start, end = head, prev
        while end:
            snxt, enxt = start.next, end.next
            start.next = end
            start = snxt
            end.next = start
            end = enxt
