# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0

        for p in prices[1:]:
            if profit < p - buy:
                profit = p - buy
            elif p < buy:
                buy = p

        return profit
        
def main():
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))

if __name__ == '__main__':
    main()