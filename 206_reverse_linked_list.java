// https://leetcode.com/problems/reverse-linked-list/description/
class Solution {
    public ListNode reverseList(ListNode head) {
        return head != null ? rec(head) : null;
    }

    public ListNode rec(ListNode root) {
        if (root.next == null) {
            return root;
        }

        ListNode n = rec(root.next);
        root.next.next = root;
        root.next = null; 

        return n;
    }

    public ListNode iter(ListNode root) {
        Stack<ListNode> stk = new Stack<>();

        ListNode curr = root;
        while (curr != null) {
            stk.push(curr);
            curr = curr.next;
        }

        if (!stk.isEmpty()) {
            root = stk.pop();
        }

        curr = root;
        while (!stk.isEmpty()) {
            ListNode n = stk.pop();

            curr.next = n;
            curr = curr.next;
        }

        if (curr != null) {
            curr.next = null;
        }

        return root;
    }
}