# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None:
            return head
        
        def traverseNode(head):
            cnt = 0
            while head is not None:
                head = head.next
                cnt += 1
            return cnt
        
        n = traverseNode(head)
        
        k %= n
        if k == 0: # for speed up?
            return head
        
        left_head = head
        cur = head
        
        from itertools import repeat # faster than range()
        for _ in repeat(None, n-k-1):
            cur = cur.next
        left_tail = cur
        right_head = cur.next
        #print(left_tail.val)
        
        for _ in repeat(None, k): # current is in left_tail position
            cur = cur.next
        right_tail = cur
        #print(right_tail.val)
        right_tail.next = left_head
        left_tail.next = None
        
        
        return right_head