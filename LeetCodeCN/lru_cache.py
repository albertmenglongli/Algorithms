class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cur_num = 0
        self.hash_map = dict()

    def _remove(self, key: int):
        self.cur_num -= 1
        node = self.hash_map[key]

        if node.prev is not None:
            prev = node.prev
            prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            next = node.next
            next.prev = node.prev
        else:
            self.tail = node.prev

        del node
        self.hash_map.pop(key, None)

    def _add_head(self, key: int, val) -> Node:
        new_head = Node(key, val)
        self.cur_num += 1
        old_head = self.head
        if old_head is not None:
            new_head.next = old_head
            old_head.prev = new_head
        else:
            self.tail = new_head
        self.head = new_head
        self.hash_map[key] = new_head
        return new_head

    def _remove_tail(self):
        tail = self.tail
        if tail is not None:
            self.hash_map.pop(tail.key, None)
            if tail.prev is not None:
                tail.prev.next = None
                self.tail = tail.prev
                del tail
            else:
                self.head = None
                self.tail = None
            self.cur_num -= 1

    def get(self, key: int) -> int:
        val = -1
        if key in self.hash_map:
            val = self.hash_map[key].val
            self._remove(key)
            self._add_head(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.hash_map:
            self._remove(key)
            head = self._add_head(key, value)
        else:
            if self.cur_num < self.capacity:
                pass
            else:
                self._remove_tail()
            head = self._add_head(key, value)
        self.hash_map[key] = head


cache = LRUCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))  # 返回 1
print(cache.put(3, 3))  # 去除 key 2
print(cache.get(2))  # 返回 -1 (未找到key 2)
print(cache.get(3))  # 返回 3
print(cache.put(4, 4))  # 去除 key 1
print(cache.get(1))  # 返回 -1 (未找到 key 1)
print(cache.get(3))  # 返回 3
print(cache.get(4))  # 返回 4

cache = LRUCache(3)
print(cache.put(2, 2))
print(cache.put(1, 1))
print(cache.get(2))
print(cache.get(1))
print(cache.get(2))
print(cache.put(3, 3))
print(cache.put(4, 4))
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
print(cache.get(4))
