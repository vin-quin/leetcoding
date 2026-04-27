// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
// Definition for a binary tree node.

import java.util.ArrayList;
import java.util.List;

public class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();

        traverse(root, 0, res);
        return res;
    }

    public void traverse(TreeNode root, int depth, List<List<Integer>> path) {
        if (root == null) {
            return;
        }

        if (path.size() <= depth) { // Fix OOB
            path.add(new ArrayList<>());
        }

        path.get(depth).add(root.val);
        traverse(root.left, depth+1, path);
        traverse(root.right, depth+1, path);
    }
}
