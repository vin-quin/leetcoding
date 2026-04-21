
/**
 * https://leetcode.com/problems/copy-list-with-random-pointer/description/
 */

import java.util.ArrayList;
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
        ArrayList<Node> a = new ArrayList();

        Node curr = head;
        while (curr != null) {

        }

        return null;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve());
    }
}
