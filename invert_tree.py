# https://leetcode.com/problems/invert-binary-tree/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert(root)
        return root

def invert(root: TreeNode):
    if not root:
        return 

    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)


def main():
    s = Solution()
    print(s.invertTree(TreeNode(None)))

if __name__ == '__main__':
    main()