from collections import deque
from typing import List


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [ [False] * len(image[0]) for r in range(len(image))]
        dx = [ 0, 0, -1, 1]
        dy = [-1, 1,  0, 0]
        queue = deque([(sr, sc)])
        v = image[sr][sc]

        while len(queue) != 0:
            r, c = queue.pop()
            image[r][c] = color

            for i in range(len(dx)):
                x = dx[i] + c
                y = dy[i] + r

                if x < 0 or x == len(image[0]) or y < 0 or y == len(image):
                    continue

                if image[y][x] == v and not visited[y][x]:
                    visited[y][x] = True
                    queue.appendleft((y, x))

        return image
