# https://leetcode.com/problems/house-robber-iii/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0

        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)

        res = max(res, self.rob(root.left) + self.rob(root.right))
        return res