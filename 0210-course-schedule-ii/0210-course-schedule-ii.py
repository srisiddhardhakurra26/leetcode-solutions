class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle, visit = set(), set()
        hm = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hm[crs].append(pre)
        res = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in hm[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
