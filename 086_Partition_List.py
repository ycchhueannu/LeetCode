# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt_dummy = ListNode(None)
        gt_dummy = ListNode(None)
        
        cur_lt = lt_dummy
        cur_gt = gt_dummy
        while head:
            if head.val < x:
                cur_lt.next = head
                cur_lt = cur_lt.next
            else:
                cur_gt.next = head
                cur_gt = cur_gt.next
            
            head = head.next
            
        cur_lt.next = gt_dummy.next
        cur_gt.next = None
        return lt_dummy.next