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
import java.util.HashMap;

class Solution {
    private HashMap<Integer,ListNode> kv = new HashMap<>();
    private ListNode head, tail;

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return new ListNode();
        }

        // We will merge into this list after we initialize this current lists kv
        this.head = lists[0]; // Our sorted list starts as our first lists arbitrarily
        ListNode curr = this.head;
        do  {
            this.kv.put(curr.val, curr);
        } while (curr.next != null);


        System.out.println(this.kv);

        for (int i = 1; i < lists.length; i++) { // Skip first list we started at
            curr = lists[i];

            while (curr != null) {
                // If we've seen this number in the kv then we need to insert it somewhere inside and do a swap
                if (this.kv.containsKey(curr.val)) {
                    this.insert(curr);
                } else if (curr.val < this.head.val) { // Else if it is less than head it must be new head
                    ListNode tmp = new ListNode(curr.val);
                    tmp.next = this.head;
                    this.head = tmp;
                } else { // Else it must be new tail
                    ListNode tmp = new ListNode(curr.val);
                    this.tail.next = tmp;
                    this.tail = tmp;
                }

                curr = curr.next;
            }
        }

        return this.head;
    }

    public void insert(ListNode n) {
        ListNode insertAt = this.kv.get(n.val);

        n.next = insertAt.next;
        insertAt.next = n;        
    }
}
