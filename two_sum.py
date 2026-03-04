# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in  range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

        return [-1, -1]

def main():
    s = Solution()
    print(s.twoSum([3,2,4], 6))

if __name__ == '__main__':
    main()