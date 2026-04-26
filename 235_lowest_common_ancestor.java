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
        dfs(root, p, s1);
        Stack<TreeNode> s2 = new Stack<>();
        dfs(root, q, s2);

        s1.retainAll(s2);

        for (TreeNode elem : s1) {
            System.out.println(elem.val);
        }

        return s1.firstElement();
    }

    public void dfs(TreeNode root, TreeNode t, Stack<TreeNode> history) {
        if (root == null) {
            history.pop();
            return;
        }

        history.push(root);
        if (root == t) {
            return;
        }

        if (root.left != null) {
            dfs(root.left, t, history);
        }

        if (root.right != null) {
            dfs(root.right, t, history);
        }
    }
}
