# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/   
class Solution:
    def solve(self, cost: list[int]) -> int:
        cost.sort()

        for i in range(len(cost)-3, -1, -2): # Every third candy iis free so set to 0
            cost[i] = 0

        return sum(cost)

def main():
    s = Solution()
    print(s.solve([1,2,3]))
    print(s.solve([6,5,7,9,2,2]))
    print(s.solve([5,5]))

if __name__ == '__main__':
    main()