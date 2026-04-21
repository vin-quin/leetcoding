/**
 * https://leetcode.com/problems/reorder-list/
 */
import java.util.Stack;
import java.lang.Math;

public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

class Solution {
    public ListNode solve(ListNode head) {
        if (head.next == null) {
            return;
        }
        Stack<ListNode> stk = new Stack();

        ListNode curr = head;
        while (curr != null) {
            stk.push(curr);
            curr = curr.next;
        }

        // We only need the top half of the stack, incl. midpoint
        // We simply iterate through and pop every other node til we hit that midpoint and its done

        int steps = Math.ceilDiv(stk.size(), 2);
        System.out.println(steps);

        curr = head;
        for (int i = 0; i < steps; i++) {
            ListNode tmp = curr.next;
            curr.next = stk.pop();
            curr.next.next = tmp;
            curr = curr.next.next;
        }

        curr.next = null; // Set tail
        
        return;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve());
    }
}