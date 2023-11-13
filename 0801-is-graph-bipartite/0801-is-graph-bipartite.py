class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph) #odd = 1, even = -1

        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[nei] and odd[i] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        odd[nei] = -1 * odd[i]
                        q.append(nei)
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True