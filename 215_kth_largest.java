// https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> Integer.compare(b, a));

        for (int n: nums) {
            q.add(n);
        }

        int n=0;
        for (int i = 0; i < k; i++){
            n = q.poll();
        }

        return n;
    }
}