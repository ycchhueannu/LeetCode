# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k == 1) or (head is None) or (head.next is None):
            return head
        
        
        prevNode = ListNode(None)
        prevNode.next = head
        ret_dummy = prevNode # store return pointer (dummy, in fact, is ret_dummy.next)
        for _ in iter(int, 1): # infinite loop
            if head is None:
                break
            start = head # store starting ListNode
            tmpList = []
            
            for i in range(0, k):
                if head is not None:
                    tmpList.append(head)
                    head = head.next
            else: # since I did not add 'break' in the if-statement above, need to add another if condition here
                if len(tmpList) < k:
                    break
            
            #nextNode = head
            #end = tmpList[-1]
            #print([i.val for i in tmpList])
            for i in range(len(tmpList)-1, 0, -1): # except index 0
                tmpList[i].next = tmpList[i-1]
            
            prevNode.next = tmpList[-1] # end
            start.next = head # nextNode
            prevNode = start
            
        return ret_dummy.next