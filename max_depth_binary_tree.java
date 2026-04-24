// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
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
    public int maxDepth(TreeNode root) {
        return dfs(root, 0);
    }

    public int dfs(TreeNode root, int d) {
        if (root == null) {
            return d;
        }

        int l = dfs(root.left, d+1);
        int r = dfs(root.right, d+1);

        return l > r ? l+1 : r+1;
    }
}