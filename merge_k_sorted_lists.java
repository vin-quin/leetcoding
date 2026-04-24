/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode head = new ListNode(Integer.MIN_VALUE); // Dummy head must be removed on return
    private ListNode tail = this.head;

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        int emptyLists = 0;
        ListNode curr;

        // Build the merged array by taking the curr of eaach list 1 at a time
        // If curr is null that list is done and skip it
        // Guarantees that the of all curr nodes is sorted
        // This process requires O(N) iteration thru lists and O(K) which is the length of the current mergeed array
        // As any time we are inserint in the middle we search up to K nodes to get insertion point
        while (emptyLists != lists.length) {
            emptyLists = 0;

            for (int i = 0; i < lists.length; i++) {
                curr = lists[i];
                if (curr == null) { // This list is done already
                    emptyLists += 1;
                    continue;
                }

                lists[i] = curr.next; // Set progress for next iter

                // If curr.val >= this.tail we can just append
                if (curr.val >= this.tail.val) {
                    curr.next = null;
                    this.tail.next = curr;
                    this.tail = curr;
                }
                // Else if curr.val <= this.head we prepend
                else if (curr.val <= this.head.val) {
                    curr.next = this.head;
                    this.head = curr;
                }
                // Else it's in the middle so walk back from the tail until curr.val <= next and insert
                else {
                    insert(curr);
                }
            }
        }

        return this.head.next;
    }

    // Walk forward until we find a val we are less than or equal to, insert there
    public void insert(ListNode n) {
        ListNode curr = this.head;

        while (curr.next != null && curr.next.val <= n.val) {
            curr = curr.next;
        }

        n.next = curr.next;
        curr.next = n;
    }
}
