class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = defaultdict()
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last 
        self.last.prev = self.first
    
    def insert(self, node):
        prevNode = self.last.prev
        prevNode.next = node
        self.last.prev = node
        node.next, node.prev = self.last, prevNode

    def delete(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self.delete(node)
            self.insert(node)
            return self.lru[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.lru:
            delnode = self.lru[key]
            self.delete(delnode)
            self.insert(node)
            self.lru[key] = node
        else:
            self.insert(node)
            self.lru[key] = node
        if len(self.lru) > self.capacity:
            lrunode = self.first.next
            self.delete(lrunode)
            del self.lru[lrunode.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)