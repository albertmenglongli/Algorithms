# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        n = 0
        currA = headA
        while currA:
            n += 1
            currA = currA.next
        m = 0
        currB = headB
        while currB:
            m += 1
            currB = currB.next
        currA = headA
        currB = headB
        if n > m:
            for i in range(0, n - m):
                currA = currA.next
        elif m > n:
            for i in range(0, m - n):
                currB = currB.next

        while currA and currB:
            if currA.val == currB.val:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        return None
     