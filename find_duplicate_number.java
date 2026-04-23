/**
 * https://leetcode.com/problems/find-the-duplicate-number/
 */
import java.util.Arrays;
class Solution {
    public Solution() {}

    public int solve(int[] nums) {
        Arrays.sort(nums);
        int lastSeen = 0;

        for (int n : nums) {
            if (n == lastSeen) {
                return n;
            }

            lastSeen = n;
        }

        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve(new int[]{1,3,4,2,2}));
    }
}