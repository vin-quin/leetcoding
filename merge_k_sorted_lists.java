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
        while (curr != null)  {
            this.kv.put(curr.val, curr);
            
            if (curr.next == null) {
                this.tail = curr;
            }

            curr = curr.next;
        } 
        
        System.out.println(this.kv);

        for (int i = 1; i < lists.length; i++) { // Skip first list we started at
            curr = lists[i];
            System.out.println(i);

            while (curr != null) {
                // If we've seen this number in the kv then we need to insert it somewhere inside and do a swap
                if (this.kv.containsKey(curr.val)) {
                    System.out.println("Contains");
                    this.insert(new ListNode(curr.val));
                } else if (curr.val < this.head.val) { // Else if it is less than head it must be new head
                    System.out.println("New head");
                    ListNode tmp = new ListNode(curr.val);
                    tmp.next = this.head;
                    this.head = tmp;
                    this.kv.put(this.head.val, this.head);
                } else { // Else it must be new tail
                    System.out.println("New tail");
                    ListNode tmp = new ListNode(curr.val);
                    this.tail.next = tmp;
                    this.tail = tmp;
                    this.kv.put(this.tail.val, this.tail);
                }

                curr = curr.next;
            }
        }
        
        System.out.println(this.kv);
        return this.head;
    }

    public void insert(ListNode n) {
        ListNode insertAt = this.kv.get(n.val);

        n.next = insertAt.next;
        insertAt.next = n;   

        this.kv.put(n.val, n);     
    }
}
