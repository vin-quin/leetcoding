// https://leetcode.com/problems/binary-tree-right-side-view/
// Definition for a binary tree node.
import java.util.ArrayList;
import java.util.List;
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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> r = new ArrayList<Integer>();
        view(root, 0, r);
        
        return r;
    }

    public void view(TreeNode root, int d, List<Integer> view) {
        if (root == null) {
            return;
        }

        if (view.size() <= d) { 
            view.add(d, root.val); // Create
        } else {
            view.set(d, root.val); // Replace
        }
        // Going left first ensure we overwrite with the rightmost which would appear in front and block the view
        view(root.left, d+1, view);
        view(root.right, d+1, view);
    }
}