class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = {i:[] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            hm[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if hm[crs] == []:
                return True
            
            visit.add(crs)
            for pre in hm[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            hm[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True