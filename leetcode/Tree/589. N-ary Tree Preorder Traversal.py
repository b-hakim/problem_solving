"""
# Definition for a Node.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution_rec:
    def preorder(self, root: 'Node') -> List[int]:
        # Preorder (Root, Left, Right)
        if root is None:
            return []

        ret = [root.val]

        for child in root.children:
            r = self.preorder(child)
            ret += r

        return ret


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        ret = []
        stack = [root]
        i = 0

        while len(stack) > 0:
            root = stack.pop()

            if root.children is not None:
                stack += reversed(root.children)

            ret.append(root.val)

        return ret
