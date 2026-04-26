// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

/**
 * Definition for a binary tree node.
 */

import java.util.Stack;
public class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}


class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        dfs(root, p, s1);
        dfs(root, q, s2);
        s1.retainAll(s2);

        return s1.lastElement();
    }

    public void dfs(TreeNode root, TreeNode target, Stack<TreeNode> history) {
        if (root == null) {
            return;
        }

        history.add(root);
        if (root == target) {
            return;
        }

        if (target.val < root.val) {
            dfs(root.left, target, history);
        } else {
            dfs(root.right, target, history);
        }
    }
}
