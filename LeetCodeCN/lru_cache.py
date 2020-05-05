class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur_num = 0
        self.hash_map = dict()

    def add_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def move_to_head(self, node):
        self.remove(node)
        self.add_head(node)

    def get(self, key: int) -> int:
        val = -1
        if key in self.hash_map:
            node = self.hash_map[key]
            val = node.val
            self.move_to_head(node)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.hash_map[key] = node
            if self.cur_num < self.capacity:
                self.cur_num += 1
            else:
                removed = self.remove_tail()
                self.hash_map.pop(removed.key, None)
            self.add_head(node)


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
