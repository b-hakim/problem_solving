# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [[root]]
        ret = []

        while len(queue) != 0:
            root = queue.pop()
            ret.append([r.val for r in root])

            neel = []

            for el in root:
                if el.left is not None:
                    neel += [el.left]
                if el.right is not None:
                    neel += [el.right]

            if len(neel) > 0:
                queue.append(neel)

        return ret
