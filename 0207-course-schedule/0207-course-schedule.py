class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        hm = collections.defaultdict(list)
        for crs, pre in pre:
            hm[crs].append(pre)
        visit = set()

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