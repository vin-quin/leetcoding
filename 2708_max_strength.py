# https://leetcode.com/problems/maximum-strength-of-a-group/    
class Solution:
    def solve(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        posIdx = -1 # first nonnegative in list

        for i in range(len(nums)):
            if nums[i] >= 0:
                posIdx = i
                break

        if posIdx == -1: # All negs in list
            if len(nums) % 2 != 0: # Uneven amount of nums in list
                nums.pop()
        elif posIdx % 2 != 0: # Odd number of negatives in list so remove last neg (this is smallest)
            nums.pop(posIdx-1)

        # if len(nums) == 1:
        #     return nums[0]
        
        score = nums[0]
        for n in nums[1:]:
            score = max(n, score*n)

        return score

def main():
    s = Solution()
    # print(s.solve([3,-1,-5,2,5,-9]))
    # print(s.solve([-4,-5,-4]))
    # print(s.solve([8,6,0,5,-4,-8,-4,9,-1,6,-4,8,-5]))
    # print(s.solve([-4,-3]))
    # print(s.solve([2,2,7,0,-4,9,4]))
    print(s.solve([3,-1,-5,2,5,-9]))

if __name__ == '__main__':
    main()