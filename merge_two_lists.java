/**
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 */

// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode solve(ListNode list1, ListNode list2) {
        ListNode head;

        if (list1 == null) {
            return list2;
        }

        if (list2 == null) {
            return list1;
        }

        // Our head always starts at the smaller value with node2 being the other list
        if (list1.val <= list2.val) {
            head = list1;
        } else {
            head = list2;
            list2 = list1; // Ovwrwrite
        }

        // Merge list2 into list1 (head)
        ListNode curr1 = head; // Head is smallest we can ever have so start at next for comparison
        ListNode curr2 = list2;

        while (curr2 != null) { // Merge it in
            if (curr1.next == null || curr2.val <= curr1.next.val) { // We are bigger than null so merge
                ListNode tmp = curr1.next;
                curr1.next = curr2;
                curr2 = curr2.next;
                curr1.next.next = tmp;
            } else {
                curr1 = curr1.next;
            }
        }

        return head;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve());
    }
}