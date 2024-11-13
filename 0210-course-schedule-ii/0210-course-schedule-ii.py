class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjList = {n : [] for n in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visit = set()
        seen = set()
        def dfs(crs):
            if crs in visit:
                return False
            if crs in seen:
                return True
            visit.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res