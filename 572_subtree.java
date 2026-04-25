// https://leetcode.com/problems/subtree-of-another-tree/description/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean found = false;
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        subtree(root, subRoot);
        return this.found;
    }

    public boolean subtree(TreeNode root, TreeNode subtree) {
        if ((root == null && subtree != null) || root != null && subtree == null) {
            return false;
        }

        if (root == null && subtree == null) {
            return true;
        }

        // Potential subtree, explore
        if (root.val == subtree.val) {
            this.found = same(root, subtree);
        }

        subtree(root.left, subtree);
        subtree(root.right, subtree);

        return false;
    }

    public boolean same(TreeNode a, TreeNode b) {
        if (a == null && b == null) {
            return true;
        }

        if ((a == null && b != null) || a != null && b == null || (a.val != b.val)) {
            return false;
        }

        return (same(a.left, b.left) == true && same(a.right, b.right) == true);
    }
}
