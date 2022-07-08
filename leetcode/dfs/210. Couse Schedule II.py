class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [[None, False] for _ in range(numCourses)]
        parent = [[] for _ in range(numCourses)]
        # children = [[] for _ in range(numCourses)]

        # for each unstarted node, loop on all requirements,
        # if there is a loop (revisiting a visited node), then return False
        # if no loop, redo step 1 untill all nodes are visited (global visited)
        adjacent_list = [[] for a in range(numCourses)]

        for edge in prerequisites:
            adjacent_list[edge[0]].append(edge[1])

        ret = []

        def can_get_prerequisits_DFS(node):
            if visited[node][0] is not None:
                return visited[node][0]

            if visited[node][1]:
                return False  # cycle exists

            visited[node][1] = True

            for req in adjacent_list[node]:
                parent[req].append(node)
                # children[node].append(req)

                req_achievable = can_get_prerequisits_DFS(req)

                if req_achievable is False:
                    visited[node][1] = False
                    return False

            visited[node][0] = True
            visited[node][1] = False
            ret.append(node)

            return True

        for i in range(numCourses):
            if not visited[i][0]:
                b = can_get_prerequisits_DFS(i)

                if not b:
                    return []

        return ret
