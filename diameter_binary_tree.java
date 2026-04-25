// https://leetcode.com/problems/diameter-of-binary-tree/description/
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
    public int diameterOfBinaryTree(TreeNode root) {
        int[] r = new int[1];
        dfs(root, r);
        return r[0];
    }

    public int dfs(TreeNode root, int[] h) {
        if (root == null) {
            return 0;
        }

        int l = dfs(root.left, h);
        int r = dfs(root.right, h);
        h[0] = Math.max(h[0], l+r);

        return 1+Math.max(l, r);
    }
}