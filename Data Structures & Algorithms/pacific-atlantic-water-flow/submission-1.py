class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N = len(heights)
        M = len(heights[0])

        marker = [[0] * len(heights[0]) for _ in range(len(heights))]
        result = list()
        def dfs(x, y, value, level):
            if x < 0 or y < 0 or x >= N or y >= M or marker[x][y] >= value or heights[x][y] < level:
                return
            
            marker[x][y] += value

            if marker[x][y] == 3:
                result.append((x, y))
            
            for i, j in ((0, 1), (0, -1), (-1, 0), (1,0)):
                dfs(x + i, y + j, value, heights[x][y])
        
        for i in range(0, N):
            dfs(i, 0, 1, 0)
        
        for j in range(0, M):
            dfs(0, j, 1, 0)
        
        for i in range(0, N):
            dfs(i, M-1, 2, 0)

        for j in range(0, M):
            dfs(N-1, j, 2, 0)
        
        return result
        
            


            
            

