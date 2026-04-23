/**
 * https://leetcode.com/problems/add-two-numbers/description/
 */
 import java.lang.Math;
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode resHead = new ListNode();
        ListNode res = resHead;
        int carry = 0;
        
        // We can just add each node we see with a carry bit if needed since we want the result as a list in the same format
        ListNode curr1 = l1, curr2 = l2;
        while (curr1 != null || curr2 != null) {
            int n1=0,n2=0;

            if (curr1 != null) {
                n1 = curr1.val;
                curr1 = curr1.next;
            }
            
            if (curr2 != null) {
                n2 = curr2.val;
                curr2 = curr2.next;
            }

            int s = n1+n2+carry;
            if (s > 9) { // Remove the tens place and add as carry for next iter
                s -= 10;
                carry = 1;
            } else {
                carry = 0;
            }

            ListNode digit = new ListNode(s);
            res.next = digit;
            res = res.next;
        }

        // We need to add a new node as the sum has a greater magnitude than its parts
        if (carry != 0) {
            res.next = new ListNode(carry);
        }

        // We always start with a leading 0 at the head so just return next for the real result
        return resHead.next;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.addTwoNumbers(l1, l2)());
    }
}