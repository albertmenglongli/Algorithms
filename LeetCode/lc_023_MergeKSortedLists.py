# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoLists(root1, root2):
            import heapq
            heap = []
            if not root1 and not root2:
                return None
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2

            cur1 = root1
            cur2 = root2
            while cur1 or cur2:
                if cur1:
                    heapq.heappush(heap, (cur1.val, cur1))
                    cur1 = cur1.next
                if cur2:
                    heapq.heappush(heap, (cur2.val, cur2))
                    cur2 = cur2.next

            list_of_nodes_in_orders = [heapq.heappop(heap)[1] for _ in range(len(heap))]

            for i in range(0, len(list_of_nodes_in_orders) - 1):
                list_of_nodes_in_orders[i].next = list_of_nodes_in_orders[i + 1]
            list_of_nodes_in_orders[-1].next = None

            return list_of_nodes_in_orders[0]

        def divide_conquer(lists):
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]

            length = len(lists)
            mid = length / 2

            left_root = divide_conquer(lists[:mid])
            right_root = divide_conquer(lists[mid:])

            new_root = mergeTwoLists(left_root, right_root)
            return new_root

        root = divide_conquer(lists)
        return root


def gen_list(lists):
    tmp = []
    for v in lists:
        tmp.append(ListNode(v))
    for i in range(len(tmp) - 1):
        tmp[i].next = tmp[i + 1]
    return tmp[0]


def print_root(root):
    res = []
    while root:
        res.append(str(root.val))
        root = root.next
    return ' -> '.join(res)


lists = [gen_list([1, 3, 5, 7]), gen_list([2, 4, 6, 8]), gen_list([12, 14, 16, 18])]

root = Solution().mergeKLists(lists)
assert print_root(root) == '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 12 -> 14 -> 16 -> 18'
