class Node:
    def __init__(self, key, val, freq=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next


class LinkedNodeList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove(self, node):
        assert len(self) >= 1
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                self.head = node.next
                node.next = None
            elif node is self.tail:
                self.tail = node.prev
                node.prev = None
            else:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
                node.prev = None
                node.next = None
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.heap = []
        self.capacity = capacity
        self.cnt = 0
        self.freq_mapping = {}
        self.key_mapping = {}

    @property
    def min_freq(self):
        return min(self.freq_mapping.keys())

    def _get_existing_node(self, key):
        node = self.key_mapping[key]
        old_freq = node.freq
        new_freq = old_freq + 1
        linked_list = self.freq_mapping[old_freq]
        linked_list.remove(node)
        if len(linked_list) == 0:
            self.freq_mapping.pop(old_freq, None)
        linked_list = self.freq_mapping.get(new_freq, None) or LinkedNodeList()
        node.freq = new_freq
        linked_list.append(node)
        self.freq_mapping[new_freq] = linked_list
        return node

    def _put_new_node(self, key, value):
        linked_list = self.freq_mapping.get(1, None) or LinkedNodeList()
        node = Node(key, value)
        self.key_mapping[key] = node
        linked_list.append(node)
        self.freq_mapping[1] = linked_list
        self.cnt += 1

    def get(self, key: int) -> int:
        val = -1
        if key in self.key_mapping:
            node = self._get_existing_node(key)
            val = node.val

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_mapping:
            node = self._get_existing_node(key)
            node.val = value
        else:
            if self.cnt < self.capacity:
                self._put_new_node(key, value)
            else:
                min_freq = self.min_freq
                linked_list = self.freq_mapping[min_freq]
                head = linked_list.head
                self.key_mapping.pop(head.key)
                linked_list.remove(head)
                del head
                if len(linked_list) == 0:
                    self.freq_mapping.pop(min_freq)
                self._put_new_node(key, value)


#
# cache = LFUCache(2)
#
# print(cache.put(1, 1))
# print(cache.put(2, 2))
# print(cache.get(1))  # 返回 1
# print(cache.put(3, 3))  # 去除 key 2
# print(cache.get(2))  # 返回 -1 (未找到key 2)
# print(cache.get(3))  # 返回 3
# print(cache.put(4, 4))  # 去除 key 1
# print(cache.get(1))  # 返回 -1 (未找到 key 1)
# print(cache.get(3))  # 返回 3
# print(cache.get(4))  # 返回 4


# cache = LFUCache(3)
# print(cache.put(2, 2))
# print(cache.put(1, 1))
# print(cache.get(2))
# print(cache.get(1))
# print(cache.get(2))
# print(cache.put(3, 3))
# print(cache.put(4, 4))
# print(cache.get(3))
# print(cache.get(2))
# print(cache.get(1))
# print(cache.get(4))

# cache = LFUCache(0)
#
# cache.put(0, 0)
# print(cache.get(0))
#
# ["LFUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
# [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]

cache = LFUCache(3)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.put(3, 3))
print(cache.put(4, 4))
print(cache.get(4))
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
print(cache.put(5, 5))
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))
