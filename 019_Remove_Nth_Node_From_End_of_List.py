# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        nPrecede = head
        for _ in range(0, n):
            if nPrecede.next is not None:
                nPrecede = nPrecede.next
            else:
                return head.next
        
        head2 = head
        for _ in iter(int, 1): # infinite loop in disguise
            if nPrecede.next is None:
                head2.next = head2.next.next
                return head
            else:
                nPrecede, head2 = nPrecede.next, head2.next