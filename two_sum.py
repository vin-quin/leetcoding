# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # one indexed result
        tried = set()
        for i in range(len(nums)):
            s = nums[i]
            if s in tried: # We won't succeed repeating this work
                continue
            for j in range(i+1, len(nums)):
                if s + nums[j] == target:
                    return [i+1, j+1]
                elif s + nums[j] > target:
                    break
            tried.add(nums[i])
        return []


def main():
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))

if __name__ == '__main__':
    main()