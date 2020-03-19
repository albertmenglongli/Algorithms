# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = str(self.val)
        if self.next is not None:
            res += "->" + str(self.next)
        return res


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        c = head
        n = c.next
        while n is not None:
            c.next = p
            p = c
            c = n
            n = n.next

        c.next = p
        head.next = None

        return c


class SolutionRecursion:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        new_head = None

        dummy = ListNode(0)
        dummy.next = head

        def inner(_head):
            nonlocal new_head

            if not _head.next:
                new_head = _head
            else:
                inner(_head.next)
                _head.next.next = _head

        inner(dummy)
        dummy.next.next = None
        return new_head


if __name__ == '__main__':
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(n1)
    head = Solution().reverseList(n1)
    print(head)
    head = SolutionRecursion().reverseList(head)
    print(head)
