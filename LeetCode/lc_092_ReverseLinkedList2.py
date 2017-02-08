# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        empty_head = ListNode(0)
        empty_head.next = head
        P_m_1 = empty_head
        for i in range(0, m - 1):
            P_m_1 = P_m_1.next
        # P_m_1 point to the m-1 Node of the original linked list
        # P_m always points to the m element of the original linked list, and will be the last one of the reversed sub linked list
        # P & P_m is a fixed pointer from now on,
        P_m =P_m_1.next
        # P_ahead is the node that will be the first node of the reversed sub linked list, a.k.k.a the one after P_m_1
        P_ahead = P_m.next

        for i in range(m, n):
            P_m.next = P_ahead.next
            P_ahead.next = P_m_1.next
            P_m_1.next = P_ahead
            P_ahead = P_m.next

        return empty_head.next



