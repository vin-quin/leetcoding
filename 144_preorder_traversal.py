# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        self.preorder(root, path)
        return path

    def preorder(self, root, path):
        if not root:
            return

        path.append(root.val)
        self.preorder(root.left, path)
        self.preorder(root.right, path)
