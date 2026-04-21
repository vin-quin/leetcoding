
/**
 * https://leetcode.com/problems/copy-list-with-random-pointer/description/
 */

import java.util.HashMap;
// Definition for a Node.

public class Node {

    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

public class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node,Node> nodeMap = new HashMap(); // Old:New

        // A map of old Node to new Node lets us iterate through O(N) the original and copy simultaneously 
        // and set them as we go so 2 O(N) ops

        Node deep = deepCopy(head, nodeMap);

        Node orig = head;
        Node copy = deep;

        while (orig != null) {
            copy.random = nodeMap.get(orig.random);

            copy = copy.next;
            orig = orig.next;
        }

        return deep;
    }

    public Node deepCopy(Node root, HashMap<Node,Node> nodeMap) {
        if (root == null) {
            return null;
        }

        Node n = new Node(root.val);
        n.next = deepCopy(root.next, nodeMap);
        nodeMap.put(root, n);
        return n;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        Node node1=new Node(1);
        Node node2=new Node(2);
        node1.next = node2;
        node1.random = node2;
        node2.random = node2;
        System.out.println(s.copyRandomList(node1));
    }
}
