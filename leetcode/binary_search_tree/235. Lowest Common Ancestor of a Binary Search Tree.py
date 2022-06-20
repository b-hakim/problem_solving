# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a, b = p, q
        p = p.val
        q = q.val

        if p == root.val or q == root.val:
            return root

        print(p, q, root.val)

        if p > q:
            p, q = q, p

        if p > root.val:
            return self.lowestCommonAncestor(root.right, a, b)

        if q < root.val:
            return self.lowestCommonAncestor(root.left, a, b)

        return root