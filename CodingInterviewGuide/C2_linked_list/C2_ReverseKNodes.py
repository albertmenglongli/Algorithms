from node import Node, generate_linked_list


def reverse_k_nodes(head, k):
    if k <= 1:
        return head
    cnt = 0
    dummy = Node(0)
    dummy.next = head
    _cur = dummy
    _start = dummy

    while _cur:
        _next = _cur.next
        if cnt == k:
            _end = _next
            _inner_cur = _start.next
            _inner_pre = _start
            while _inner_cur != _end:
                _inner_next = _inner_cur.next
                _inner_cur.next = _inner_pre
                _inner_pre = _inner_cur
                _inner_cur = _inner_next
            _last_node_of_cur_reversed_sub_linked_list = _start.next
            _last_node_of_cur_reversed_sub_linked_list.next = _end
            _start.next = _inner_pre
            _start = _last_node_of_cur_reversed_sub_linked_list

            cnt = 0

        cnt += 1
        _cur = _next

    return dummy.next


head = generate_linked_list(range(1, 10))
print(head)
print(reverse_k_nodes(head, 3))
