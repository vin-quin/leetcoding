# https://leetcode.com/problems/invert-binary-tree/description/
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
    # print(s.solve())

if __name__ == '__main__':
    main()