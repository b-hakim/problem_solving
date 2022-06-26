# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        #         if root.left is None and root.right is None:
        #             return targetSum == root.val

        path = [root.val]
        running_sum = 0

        def dfs(r):
            nonlocal running_sum
            print(running_sum + 1)
            running_sum += r.val

            if r.left is None and r.right is None:
                return running_sum == targetSum

            # first check if current node achieves the required sum
            # Only used if the path doesn't have to be "to the leaf"
            # if running_sum == targetSum:
            #     return True

            # check left
            if r.left is not None:
                path.append(r.left.val)

                if dfs(r.left):
                    return True

                path.pop()
                running_sum -= r.left.val

            if r.right is not None:
                path.append(r.right.val)
                if dfs(r.right):
                    return True
                path.pop()
                running_sum -= r.right.val

            return False

        return dfs(root)

