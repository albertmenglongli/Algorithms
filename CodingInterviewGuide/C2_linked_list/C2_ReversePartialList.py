from node import Node, generate_linked_list


def revers_partial_list(head, para_from, para_to):
    dummy_head = Node(0)
    dummy_head.next = head
    _cur = dummy_head
    # increase _from and _to, due to dummy_head is included
    _from = para_from + 1
    _to = para_to + 1
    _len = 0
    _start = _end = None
    while _cur:
        _len += 1

        if _len == _from - 1:
            _start = _cur
        if _len == _to + 1:
            _end = _cur

        _cur = _cur.next

    if _from <= 0 or _from >= _to or _to > _len:
        return head

    _pre = None
    _cur = _start.next
    # the following part take ReverseList as reference
    while _cur != _end:
        _next = _cur.next
        _cur.next = _pre
        _pre = _cur
        _cur = _next
    # link the three parts: start + reversed_list + end
    # _end could be None, if _to is the last node of the original linked list
    _start.next.next = _end
    _start.next = _pre

    return dummy_head.next


head = generate_linked_list(range(1, 6))
assert str(revers_partial_list(head, 2, 3)) == '1->3->2->4->5'

head = generate_linked_list(range(1, 6))
assert str(revers_partial_list(head, 1, 5)) == '5->4->3->2->1'

head = generate_linked_list(range(1, 6))
assert str(revers_partial_list(head, 2, 4)) == '1->4->3->2->5'
