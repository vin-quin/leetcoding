# https://leetcode.com/problems/maximum-strength-of-a-group/    
class Solution:
    def solve(self, nums: list[int]) -> int:
        nums.sort()
        posIdx = -1 # first nonnegative in list

        for i in range(len(nums)):
            if nums[i] >= 0:
                posIdx = i
                break

        if posIdx == -1: # No positives in list remove last
            nums.pop()
        elif posIdx  % 2 != 0: # Odd number of negatives in list so remove last neg (this is smallest)
            nums.pop(posIdx-1)

        score = 1
        for n in nums:
            score *= n

        return score

def main():
    s = Solution()
    print(s.solve([3,-1,-5,2,5,-9]))
    print(s.solve([-4,-5,-4]))

if __name__ == '__main__':
    main()