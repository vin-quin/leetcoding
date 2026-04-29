/* 
https://leetcode.com/problems/clone-graph/
*/

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Node,Node> seen = new HashMap<Node,Node>();
        dfs(node, seen);
        return seen.get(node); // Get copied head
    }


    public Node dfs(Node node, HashMap<Node,Node> seen) {
        if (node == null) {
            return null;
        }
        
        if (seen.containsKey(node)) {
            return seen.get(node);
        }

        Node copy = new Node(node.val);
        seen.put(node, copy);

        for (Node n : node.neighbors) {
            Node c = dfs(n, seen);
            copy.neighbors.add(c);
        }

        return copy;
    }
}