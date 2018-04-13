# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur is not None:
            if cur.val != prev.val: prev = cur
            else: prev.next = cur.next
            
            cur = cur.next
        
        return dummy.next