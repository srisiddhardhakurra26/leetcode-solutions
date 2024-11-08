class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict()
        self.leftmost = Node(0, 0)
        self.rightmost = Node(0, 0)
        self.leftmost.next = self.rightmost
        self.rightmost.prev = self.leftmost

    def insert(self, node):
        left = self.rightmost.prev
        left.next = node
        self.rightmost.prev = node
        node.next, node.prev = self.rightmost, left

    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.leftmost.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)