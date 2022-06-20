# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, ret = self.isValidBST_non_root(root)
        return ret

    def isValidBST_non_root(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None, None, True

        left_left_most, left_right_most, valid_subtree1 = self.isValidBST_non_root(root.left)
        right_left_most, right_right_most, valid_subtree2 = self.isValidBST_non_root(root.right)

        valid_subtree3 = True

        if root.left is not None:
            valid_subtree3 = root.val > root.left.val
            valid_subtree3 = valid_subtree3 and root.val > left_right_most
        else:
            left_left_most = root.val

        if root.right is not None:
            valid_subtree3 = valid_subtree3 and root.val < root.right.val
            valid_subtree3 = valid_subtree3 and root.val < right_left_most
        else:
            right_right_most = root.val

        valid_subtree = valid_subtree1 and valid_subtree2 and valid_subtree3

        return left_left_most, right_right_most, valid_subtree


