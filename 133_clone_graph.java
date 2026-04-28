/* 
https://leetcode.com/problems/clone-graph/
*/

import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
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


        return walk(node);
    }

    public Node walk(Node original) {
        Node copy = new Node(original.val);
        ArrayList<Node> q = new ArrayList<Node>(original);
        ArrayList<Node> copyQ = new ArrayList<Node>(copy);
        HashSet<Integer> seen = new HashSet<>();

        while (!q.isEmpty()) {
            Node o = q.removeFirst();
            Node c = copyQ.removeFirst();
            
            if (seen.contains(o.val)) {
                continue;
            }

            seen.add(o.val);

            for (Node neighbor : o.neighbors) {
                Node n = new Node(neighbor.val);
                c.neighbors.add(n);
                q.add(neighbor);
                copyQ.add(n);
            }
        }

        return copy;
    }

    // public void copy(Node original, Node copy) {
    //     copy = new Node(original.val);

    //     for (Node n: original.neighbors) {
    //         copy(n, )
    //     }
    // }
}