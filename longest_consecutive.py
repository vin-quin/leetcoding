# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def solve(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1
        consecutive = 1
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                consecutive += 1

                if consecutive > longest:
                    longest = consecutive
            elif nums[i] == nums[i-1]: # We can still be consecutive since we are the same num
                continue
            else:
                consecutive = 1

        return longest

def main():
    s = Solution()
    print(s.solve([100,4,200,1,3,2]))
    print(s.solve([0,3,7,2,5,8,4,6,0,1]))
    print(s.solve([1,0,1,2]))

if __name__ == '__main__':
    main()