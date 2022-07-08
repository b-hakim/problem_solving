class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest_increasing_path = []

        for l in range(len(matrix)):
            longest_increasing_path.append([-1] * len(matrix[0]))

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        stack = []

        # [[3, 6], [1, 5], [3, 4]]
        # [[F, 1], [F, F], [F, F]] .. longest_increasing_path
        #

        def dfs(row, col):

            if longest_increasing_path[row][col] != -1:
                return longest_increasing_path[row][col]

            max_LIP = 1

            for k in range(len(dx)):
                n_row, n_col = row + dx[k], col + dy[k]

                if n_row < 0 or n_col < 0 or n_row == len(matrix) or n_col == len(matrix[i]):
                    continue

                if matrix[n_row][n_col] > matrix[row][col]:
                    c = dfs(n_row, n_col) + 1
                    if c > max_LIP:
                        max_LIP = c

            longest_increasing_path[row][col] = max_LIP
            return max_LIP

        max_path = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if longest_increasing_path[i][j] == -1:
                    m = dfs(i, j)

                    if m > max_path:
                        max_path = m

        return max_path


