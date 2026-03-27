# https://leetcode.com/problems/missing-number/description/
class Solution:
    def solve(self, nums: list[int]) -> int:
        numSum, targetSum = 0, len(nums)
        
        for i in range(len(nums)):
            targetSum += i
            numSum += nums[i]
        
        return targetSum - numSum

def main():
    s = Solution()
    print(s.solve([3,0,1]))
    print(s.solve([0,1]))
    print(s.solve([9,6,4,2,3,5,7,0,1]))

if __name__ == '__main__':
    main()