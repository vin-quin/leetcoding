// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
class Solution {
    public int maxDepth(TreeNode root) {
        return dfs(root);
    }

    public int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        return Math.max(dfs(root.left), dfs(root.right))+1;
    }
}