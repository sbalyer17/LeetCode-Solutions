# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        multiplier = 1
        sum1 = 0
        
        while l1 != None:
            sum1 += l1.val * multiplier
            l1 = l1.next
            multiplier *= 10
            
        multiplier = 1
            
        while l2 != None:
            sum1 += l2.val * multiplier
            l2 = l2.next
            multiplier *= 10
            
        head = None
        current = None
        i = 0
        
        if (sum1 == 0):
            return ListNode(0)
            
        while sum1 > 0:
            lastDigit = sum1%10
            sum1 //= 10
            l3 = ListNode(val = lastDigit)
            if i == 0:
                head = l3
            if current:
                current.next = l3
            current = l3
            i += 1
            
        return head
