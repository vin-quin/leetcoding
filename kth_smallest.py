# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, vals=[]):
            if root.left:
                inOrder(root.left, vals)
            vals.append(root.val)
            if root.right:
                inOrder(root.right, vals)
            
            return vals

        v = inOrder(root, [])

        return v[k-1]

def main():
    s = Solution()
    print(s.solve())

if __name__ == '__main__':
    main()
    