# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def solve(self, nums: list[int]) -> int:
        score, count = 0, 0

        for n in nums:
            if n == 1:
                count += 1
            else: 
                count = 0
            
            score = max(score, count)

        return score

def main():
    s = Solution()
    print(s.solve([1,1,0,1,1,1]))

if __name__ == '__main__':
    main()