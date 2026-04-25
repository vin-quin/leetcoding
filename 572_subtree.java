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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return subtree(root, subRoot);
    }

    public boolean subtree(TreeNode root, TreeNode subtree) {
        if (root == null) {
            return false;
        }

        if (subtree == null) {
            return true;
        }

        // Potential subtree, explore
        if (same(root, subtree)) {
            return true;
        }

        return subtree(root.left, subtree) || subtree(root.right, subtree);
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
