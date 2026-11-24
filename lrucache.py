class Node:
    def __init__(self, key, value, prev=None, next_node=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_node

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node):
        last = self.tail.prev

        node.prev = last
        node.next = self.tail

        last.next = node
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_end(node)

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # 10

cache.put(3, 30)
print(cache.get(2))  # -1

cache.put(4, 40)
print(cache.get(1))  # -1
print(cache.get(3))  # 30
print(cache.get(4))  # 40