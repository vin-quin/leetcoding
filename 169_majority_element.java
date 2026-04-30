// https://leetcode.com/problems/majority-element/description/
class Solution {
    public int majorityElement(int[] nums) { // A majority means the midpoint should always contain the most frequent value
        Arrays.sort(nums);
        return nums[nums.length/2];
    }

    // public int divide(int[] nums, int l, int r) {
    //     // Split at midpoint until the array is 1/2 elements
    //     // Return that majority

    //     if (r-l+1 < 3) { // We have 1 or 2 elements so it's just a 50/50 which is majority, pick safe option
    //         this.freq
    //         return nums[l];
    //     }

    //     int mid = (r-l)+l / 2;
    //     divide(nums, l, mid-1);
    //     divide(nums, mid+1, r);
    // }
}