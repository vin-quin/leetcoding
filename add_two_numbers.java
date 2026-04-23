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
        int[] nums1 = new int[9];
        int[] nums2 = new int[9];

        // Get the digits in each num, worst casse 9 iters
        int i = 8;
        ListNode curr1 = l1, curr2 = l2;
        while (curr1 != null || curr2 != null) {
            if (curr1 != null) {
                nums1[i] = curr1.val;
                curr1 = curr1.next;
            }
            
            if (curr2 != null) {
                nums2[i] = curr2.val;
                curr2 = curr2.next;
            }

            i--;
        }

        System.out.println(nums1);
        System.out.println(nums2);

        // Convert nums to actual ints
        int num1=0, num2=0;
        int exp = 8;

        // N * 10^exp = digit's real value for its pos
        for (i = 0; i < nums1.length; i++) {
            num1 += nums1[i] * Math.pow(10, exp);
            exp--;
        }

        exp=8;
        // N * 10^exp = digit's real value for its pos
        for (i = 0; i < nums2.length; i++) {
            num2 += nums2[i] * Math.pow(10, exp);
            exp--;
        }

        System.out.println(num1);
        System.out.println(num2);

        int res = num1+num2;
        ListNode resHead = new ListNode(0);
        // Rebuild res as a list in same format and return that node

        return resHead;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.addTwoNumbers(l1, l2)());
    }
}