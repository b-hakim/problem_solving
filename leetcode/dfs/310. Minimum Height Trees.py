from typing import List


class Solution_TLE:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def DFS(root, prev):
            max_height = 0

            for edge in edges:
                if edge[0] == root and edge[1] != prev:
                    height = DFS(edge[1], root) + 1
                elif edge[1] == root and edge[0] != prev:
                    height = DFS(edge[0], root) + 1
                else:
                    height = 0

                if height > max_height:
                    max_height = height

            return max_height

        min_height = 10 ** 5
        list_roots = []

        for i in range(n):
            max_height = DFS(i, -1)

            if max_height < min_height:
                list_roots = [i]
                min_height = max_height
            elif max_height == min_height:
                list_roots.append(i)
                min_height = max_height

        return list_roots


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adjacent_list = [[] for i in range(n)]

        for edge in edges:
            adjacent_list[edge[0]].append(edge[1])
            adjacent_list[edge[1]].append(edge[0])

        best_path = [-1] * n
        visited = [False] * n

        def DFS(root):
            max_height = 0
            best_child = -1
            visited[root] = True

            for c in adjacent_list[root]:
                if not visited[c]:
                    curr_height = DFS(c) + 1

                    if curr_height > max_height:
                        max_height = curr_height
                        best_child = c

            if best_child != -1:
                best_path[root] = best_child

            visited[root] = False
            return max_height

        # start from node 0 to farthest node
        # find farthest node again and track its length
        # find the middle node(s)
        root = 0

        DFS(root)
        last_child = root

        while best_path[last_child] != -1:
            last_child = best_path[last_child]

        print(best_path, last_child)

        best_path = [-1] * n

        DFS(last_child)

        print(best_path, last_child)

        root = last_child
        slow = root
        fast = root
        c = 0

        while best_path[fast] != -1 and best_path[best_path[fast]] != -1:
            slow = best_path[slow]
            fast = best_path[best_path[fast]]
            print(slow, fast, end=" | ")

        print()
        print(slow, fast)

        # slow is on the middle
        if best_path[fast] == -1:  # fast reached the end and its odd num
            return [slow]
        else:
            return [slow, best_path[slow]]