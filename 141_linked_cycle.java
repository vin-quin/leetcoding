// https://leetcode.com/problems/linked-list-cycle/description/
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode slow=head,fast=head;

        while (slow.next != null && fast.next != null && fast.next.next != null) {
            // Eventually fast will reach slow if there is a cycle, otherwise we will hit a dead end
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}