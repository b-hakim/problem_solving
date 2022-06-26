# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        path = [root.val]
        running_sum = root.val
        accepted_paths = []

        def dfs(r):
            nonlocal running_sum, path

            if r.left is None and r.right is None:

                if running_sum == targetSum:
                    accepted_paths.append(path.copy())
                return

            if r.left is not None:
                path.append(r.left.val)
                running_sum += r.left.val
                dfs(r.left)
                path.pop()
                running_sum -= r.left.val

            if r.right is not None:
                path.append(r.right.val)
                running_sum += r.right.val
                dfs(r.right)
                path.pop()
                running_sum -= r.right.val

        dfs(root)
        return accepted_paths

