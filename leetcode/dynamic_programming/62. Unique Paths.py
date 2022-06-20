class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dix = [-1, 1, 0, 0]
        diy = [0, 0, -1, 1]

        visited = [[]] * n
        costs = [[]] * n

        for i in range(n):
            visited[i] = [False] * m
            costs[i] = [0] * m

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    visited[i][j] = True
                    costs[i][j] = 1
                    continue

                c = 0

                for v in range(len(dix)):
                    dy = diy[v] + i
                    dx = dix[v] + j

                    if dx < 0 or dx == m or dy < 0 or dy == n:
                        continue

                    # if j == 1 and i == 0:
                    #     print(dy, dx, visited[dy][dx])

                    if visited[dy][dx]:
                        c += costs[dy][dx]
                        # print(costs[dy][dx])

                costs[i][j] = c
                visited[i][j] = True
                # print(costs[i][j], end=" ")
            # print()

        return costs[n - 1][m - 1]
