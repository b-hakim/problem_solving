from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        num_islands = 0
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]

        def BFS(row, col):
            nonlocal grid
            queue = deque([(row, col)])

            while len(queue) > 0:
                r, c = queue.pop()

                for i in range(len(dr)):
                    nr, nc = dr[i] + r, dc[i] + c

                    if nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or grid[nr][nc] == '0':
                        continue

                    grid[nr][nc] = '0'
                    queue.appendleft((nr, nc))

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    BFS(row, col)
                    num_islands += 1

        return num_islands