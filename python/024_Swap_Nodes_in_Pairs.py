# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None): # 0 node or 1 node
            return head
        dummy = ListNode(None)
        #dummy.next = head
        prevNode, nextNode = head, head.next # swap pairs
        pp = dummy # prevNode's previous node, short for prevPrev
        while nextNode is not None:
            pp.next = nextNode
            nn = nextNode.next # nextNode's next node, short for nextNext
            nextNode.next = prevNode
            prevNode.next = nn
            # update
            pp = prevNode 
            prevNode = prevNode.next
            nextNode = prevNode.next if prevNode is not None else None
        return dummy.next