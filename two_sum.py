# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # one indexed result
        l, r = 0, len(nums)-1

        while nums[l] + nums[r] != target:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

        return [l+1, r+1]


def main():
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))

if __name__ == '__main__':
    main()