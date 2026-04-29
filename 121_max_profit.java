// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy = Integer.MAX_VALUE;

        for (int p: prices) {
            if (p < buy) {
                buy = p;
            } else {
                profit = Math.max(profit, p-buy);
            }
        }

        return profit;
    }
}