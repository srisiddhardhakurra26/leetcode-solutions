class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src : [] for src, dest in tickets}
        for src, dest in tickets:
            adj[src].append(dest)
        
        stack = ["JFK"]
        res = []
        while stack:
            cur = stack[-1]
            if cur in adj and adj[cur]:
                dst = adj[cur].pop(0)
                stack.append(dst)
            else:
                res.append(stack.pop())
        return res[::-1]