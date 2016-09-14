class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # the first ListNode for result is just a placeholder, will be removed when return
        l3 = ListNode(0)
        h1, h2, h3, carry = l1, l2, l3, 0
        while h1 or h2:
            val =  carry
            val += h1.val if h1 else 0
            val += h2.val if h2 else 0

            carry = val / 10
            h3.next = ListNode(val % 10)

            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            h3 = h3.next

        if carry:
            h3.next = ListNode(carry)

        return l3.next
