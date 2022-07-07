from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [[None, False] for _ in range(numCourses)]

        # for each unstarted node, loop on all requirements,
        # if there is a loop (revisiting a visited node), then return False
        # if no loop, redo step 1 untill all nodes are visited (global visited)
        adjacent_list = [[] for a in range(numCourses)]

        for edge in prerequisites:
            adjacent_list[edge[0]].append(edge[1])

        print(adjacent_list)

        def can_get_prerequisits_DFS(node):
            if visited[node][0] is not None:
                return visited[node][0]

            if visited[node][1]:
                return False  # cycle exists

            visited[node][1] = True

            for req in adjacent_list[node]:
                req_achievable = can_get_prerequisits_DFS(req)

                if req_achievable is False:
                    visited[node][1] = False
                    return False

            visited[node][0] = True
            visited[node][1] = False
            return True

        for i in range(numCourses):
            if not visited[i][0]:
                b = can_get_prerequisits_DFS(i)

                if not b:
                    return False

        return True
