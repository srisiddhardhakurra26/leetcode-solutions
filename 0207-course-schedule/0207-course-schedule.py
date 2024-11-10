class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if crs not in adjList:
                return True
            visit.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adjList[crs] = []
            return True
        res = True
        for n in range(numCourses):
            res = res and dfs(n)
        return res