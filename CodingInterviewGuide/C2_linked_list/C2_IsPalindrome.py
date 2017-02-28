from node import generate_linked_list


def is_palindrome(head):
    stack = list()
    _cur = head
    while _cur:
        stack.append(_cur.value)
        _cur = _cur.next

    _cur = head

    while stack:
        if _cur.value != stack.pop():
            return False
        else:
            _cur = _cur.next
    else:
        return True


def is_palindrome3(head):
    if not head or not head.next:
        return True
    mid = head
    end = head
    while end.next and end.next.next:
        mid = mid.next
        end = end.next.next

    right_head_before_reverse = mid
    _cur = right_head_before_reverse
    _pre = None
    while _cur:
        _next = _cur.next
        _cur.next = _pre
        _pre = _cur
        _cur = _next

    _right_start = _pre
    is_palindrome_flag = True
    _left_cur = head
    _right_cur = _right_start

    while _left_cur and _right_cur:
        if _left_cur.value != _right_cur.value:
            is_palindrome_flag = False
            break
        _left_cur = _left_cur.next
        _right_cur = _right_cur.next

    _cur = _right_start
    _pre = None
    while _cur:
        _next = _cur.next
        _cur.next = _pre
        _pre = _cur
        _cur = _next
    return is_palindrome_flag


head = generate_linked_list([1, 2, 3, 2, 1])
assert is_palindrome(head)
head = generate_linked_list([1, 2, 3, 1, 1])
assert not is_palindrome(head)

head = generate_linked_list([1, 2, 3, 2, 1])
assert is_palindrome3(head)

head = generate_linked_list([1, 2, 3, 3, 2, 1])
assert is_palindrome3(head)
