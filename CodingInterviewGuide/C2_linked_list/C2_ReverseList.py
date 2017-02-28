from node import generate_linked_list


def reverse_list(head):
    if not head or not head.next:
        return head
    _pre = None
    _cur = head

    while _cur:
        _next = _cur.next
        _cur.next = _pre
        _pre = _cur
        _cur = _next
    return _pre


def reverse_list_with_comments(head):
    if not head or not head.next:
        return head
    _pre = None
    _cur = head

    while _cur:
        #  x    pre   cur
        # [] <- []    [] -> [] -> []
        _next = _cur.next

        #  x    pre   cur   next
        # [] <- []    [] -> [] -> []

        _cur.next = _pre

        #  x    pre   cur   next
        # [] <- [] <- []    [] -> []

        _pre = _cur
        _cur = _next

        #  x     xx   pre   cur
        # [] <- [] <- []    [] -> []

    # when end of loop
        #  x     xx   xxx   xxxx  pre  cur
        # [] <- [] <- [] <- [] <- []   None
    return _pre


values = [1, 2, 3, 4, 5]
head = generate_linked_list(values)
print head
print reverse_list(head)
