import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test Case 1: Standard case
        int[] nums1 = {1, 3, -1, -3, 5, 3, 6, 7};
        int k1 = 3;
        System.out.println("Test 1: " + Arrays.toString(sol.maxSlidingWindow(nums1, k1)));
        // Expected: [3, 3, 5, 5, 6, 7]

        // // Test Case 2: Window size of 1
        // int[] nums2 = {1};
        // int k2 = 1;
        // System.out.println("Test 2: " + Arrays.toString(sol.maxSlidingWindow(nums2, k2)));
        // // Expected: [1]

        // // Test Case 3: All negative numbers
        // int[] nums3 = {-7, -8, -7, 5, 7, 1, 6, 0};
        // int k3 = 4;
        // System.out.println("Test 3: " + Arrays.toString(sol.maxSlidingWindow(nums3, k3)));
        // Expected: [5, 7, 7, 7, 7]
    }
}

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        return null;
    }
}