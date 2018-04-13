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
        d = {}
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur is not None:
            if cur.val not in d:
                d[cur.val] = None
                
                try: 
                    if cur.next.val != cur.val:
                        prev.next = cur
                        prev = cur
                except:
                    prev.next = cur
                    prev = cur
            
            cur = cur.next
        prev.next = None # = cur
        
        return dummy.next