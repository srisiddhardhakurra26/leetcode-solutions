class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        visit = [0] * numCourses  # 0 represents unvisited, 1 represents visiting, 2 represents visited
        output = []

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if visit[crs] == 1:
                return False
            if visit[crs] == 2:
                return True

            visit[crs] = 1
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visit[crs] = 2
            output.append(crs)
            return True

        for i in range(numCourses):
            if visit[i] == 0:
                if not dfs(i):
                    return []
        return output
