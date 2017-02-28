from node import generate_linked_list


def list_partition(head, pivot):
    small_head = None
    small_tail = None
    equal_head = None
    equal_tail = None
    large_head = None
    larget_tail = None
    while head:
        next = head.next
        head.next = None
        if head.value < pivot:
            if small_head is None:
                small_head = small_tail = head
            else:
                small_tail.next = head
                small_tail = small_tail.next
        elif head.value == pivot:
            if equal_head is None:
                equal_head = equal_tail = head
            else:
                equal_tail.next = head
                equal_tail = equal_tail.next
        else:
            if large_head is None:
                large_head = larget_tail = head
            else:
                larget_tail.next = head
                larget_tail = larget_tail.next
        head = next

    if equal_tail:
        equal_tail.next = large_head
    else:
        equal_head = large_head

    if small_tail:
        small_tail.next = equal_head
    else:
        small_head = equal_head
    return small_head


head = generate_linked_list([7, 9, 1, 7, 5, 2, 5])
assert str(list_partition(head, 5)) == '1->2->5->5->7->9->7'
head = generate_linked_list([7, 9, 8, 7])
assert str(list_partition(head, 5)) == '7->9->8->7'
head = generate_linked_list([5, 5, 5, 5])
assert str(list_partition(head, 5)) == '5->5->5->5'
head = generate_linked_list([1, 2, 3, 1])
assert str(list_partition(head, 5)) == '1->2->3->1'
