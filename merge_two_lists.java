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
        ListNode node2;
        ListNode head;

        // Our head always starts at the smaller value with node2 being the other list
        if (list1.val <= list2.val) {
            head = list1;
            node2 = list2;
        } else {
            head = list2;
            node2 = list1;
        }

        ListNode node = head;

        while (node2 != null) {
            if (node2.val < node.val) { // Merge in its smaller
                ListNode tmp = node;
                node = node2;
                node.next = tmp;
                node2 = node2.next;
            } else { 
                node = node.next;
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