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
        ListNode slow = head;
        ListNode fast =  head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse from slow to end
        ListNode prev = null;
        ListNode next = slow.next;
        slow.next = null; // This wil be tail

        while (next != null) {
            ListNode tmp = next.next;
            next.next = prev;
            prev = next;
            next = tmp;
        }

        // Merge
        ListNode node = head;

        while (prev != null) {
            ListNode tmp = node.next, tmp2 = prev.next;
            node.next = prev;
            prev.next = tmp;
            node = tmp;
            prev = tmp2;
        }
    }
}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve());
    }
}