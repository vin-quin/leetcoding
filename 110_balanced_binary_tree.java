// https://leetcode.com/problems/balanced-binary-tree/description/

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
    public boolean isBalanced(TreeNode root) {
        // For every node, the heights of left and right subtrees differ by at most 1.
        return rec(root) != -1; // -1 = Unbalanced
    }

    public int rec(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int l = rec(root.left);
        if (l < 0) {
            return l;
        }
        
        int r = rec(root.right);
        if (r < 0) {
            return r;
        }

        if (Math.abs(l-r) > 1){
            return -1;
        }

        return 1+Math.max(l,r);
    }
}
