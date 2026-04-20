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
        // Take the max of EACH window and add that. Same logic applies the first
        // Window is our starting max and it only changes by 1 each time so
        // A single check tells us the new max in the current window
        // O(N)

        // Monotonically increasing stack of size k
        // Store as pairs of (index,value)
        // If index is OOB pop it its dead forever
        // Else if new N is a new max we can clear the stack
        //  Because we're guaranteed this new max at minimum for the next K elements

        // Store the index of the max in THIS window
        // If new int is BIGGER than max
            // We update the new max it and continue no scan needed
        // If index is out of bounds 
            // We need to scan this window again fora new max


        // The first window is the initial max window
        int[] maxWindow = new int[nums.length];
        int maxN = nums[0]; // Biggest num in max window. This must be exceeded to take a new max

        // We check the initial k elements to get the starting max
        for (int i = 1; i < k; i++) {
            if (nums[i] > maxN) {
                maxN = nums[i];
            }
        }

        // Check each next in window til we are done

        return maxWindow;
    }
}