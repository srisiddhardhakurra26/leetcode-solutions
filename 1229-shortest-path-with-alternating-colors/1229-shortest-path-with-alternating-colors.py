class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)
        q = collections.deque()
        answer = [-1] * n
        visit = set()

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        q.append([0, 0, None])
        while q:
            node, length, color = q.popleft()
            if answer[node] == -1:
                answer[node] = length
            
            if color != "RED":
                for nei in red[node]:
                    if(nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append([nei,length + 1, "RED"])
            if color != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append([nei, length + 1, "BLUE"])
        return answer