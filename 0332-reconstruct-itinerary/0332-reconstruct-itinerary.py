class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        for src in adj:
            adj[src].sort()

        res = []
        stack = ["JFK"]

        while stack:
            curr = stack[-1]
            if curr in adj and adj[curr]:
                next_dest = adj[curr].pop(0)
                stack.append(next_dest)
            else:
                res.append(stack.pop())

        return res[::-1]
