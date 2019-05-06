# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        digit, carry = (l1.val + l2.val) % 10, (l1.val + l2.val) // 10
        head = ListNode(digit)
        hptr = head # head pointer
        ptr1, ptr2 = l1.next, l2.next
        
        while (ptr1 is not None) and (ptr2 is not None):
            digit, carry = (ptr1.val + ptr2.val + carry) % 10, (ptr1.val + ptr2.val + carry) // 10
            tmp = ListNode(digit)
            hptr.next = tmp
            hptr = tmp
            ptr1, ptr2 = ptr1.next, ptr2.next
            
        while ptr1 is not None:
            digit, carry = (ptr1.val + carry) % 10, (ptr1.val + carry) // 10
            tmp = ListNode(digit)
            hptr.next = tmp
            hptr = tmp
            ptr1 = ptr1.next
        
        while ptr2 is not None:
            digit, carry = (ptr2.val + carry) % 10, (ptr2.val + carry) // 10
            tmp = ListNode(digit)
            hptr.next = tmp
            hptr = tmp
            ptr2 = ptr2.next
        
        if carry != 0:
            tmp = ListNode(carry)
            hptr.next = tmp
            
        return head