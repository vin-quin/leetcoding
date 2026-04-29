// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        bfs(root, 0, res);
        return res;
    }

    public void bfs(TreeNode root, int depth, List<List<Integer>> res) {
        if (root == null) {
            return;
        }

        // If array exists at depth in res, append else create
        if (depth >= res.size()) {
            res.add(new ArrayList<Integer>());
        }
        res.get(depth).add(root.val);

        bfs(root.left, depth+1, res);
        bfs(root.right, depth+1, res);
    }
}