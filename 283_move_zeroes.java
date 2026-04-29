// https://leetcode.com/problems/move-zeroes/description/
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1) {
            return;
        }

        // Immediately put nonzeroes at the insertIdx andwe just append htme at the end
        int insertAt = 0;
        int zeroes = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[insertAt] = nums[i];
                insertAt++; // Move to maintain order
            } else {
                zeroes++;
            }
        }

        for (int i=0; i < zeroes; i++) {
            nums[insertAt] = 0;
            insertAt++;
        }
    }
}