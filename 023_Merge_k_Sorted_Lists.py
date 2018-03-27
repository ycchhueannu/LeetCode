# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        vList = []
        if all(i is None for i in lists):
            return []
        
        k = len(lists)
        for i in range(0, k):
            ptr = lists[i]
            for _ in iter(int, 1):
                if ptr is None:
                    break
                vList.append(ptr.val)
                ptr = ptr.next
            
        vList.sort()
        
        if vList == []:
            return []
        
        head = pre = ListNode(None) # head contains dummy val 'None'
        for v in vList:
            cur = ListNode(v)
            pre.next = cur
            pre = pre.next
        return head.next