// https://leetcode.com/problems/same-tree/description/

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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        return same(p, q);
    }

    public boolean same(TreeNode a, TreeNode b) {
        if (a == null && b == null) {
            return true;
        }

        if ((a == null && b != null)
                || (a != null && b == null)
                || (a.val != b.val)) {
            return false;
        }

        if (!same(a.left, b.left)) {
            return false;
        }

        if (!same(a.right, b.right)) {
            return false;
        }

        return true;
    }
}
