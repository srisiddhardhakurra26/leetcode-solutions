"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        nodes = defaultdict()
        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next
        for node in nodes.keys():
            nodes[node].next = nodes[node.next] if node.next else None
            nodes[node].random = nodes[node.random] if node.random else None
        return nodes[head] if head else None