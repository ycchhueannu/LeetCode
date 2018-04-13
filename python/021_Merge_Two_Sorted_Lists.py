# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        head = cur = ListNode(None)
        
        while (l1 is not None) and (l2 is not None):
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
                
        while l1 is not None:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        while l2 is not None:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        return head.next