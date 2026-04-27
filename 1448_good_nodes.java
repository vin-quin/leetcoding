// https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private int good = 0;

    public int goodNodes(TreeNode root) {
        // Good IF Root to node contains no value greater than node (including root)

        dfs(root, Integer.MIN_VALUE);

        return this.good;
    }

    // DFS with a max lets us check at each node
    public void dfs(TreeNode root, int max) {
        if (root == null) {
            return;
        }

        if (max <= root.val) { 
            this.good += 1;
            max = root.val;
        } 

        dfs(root.left, max);
        dfs(root.right, max);
    }
}