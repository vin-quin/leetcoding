# https://leetcode.com/problems/combination-sum-ii/description/
# 
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        backtrack(candidates, target, 0, [], 0, res)

        return res

def backtrack(nums: list[int], target: int, idx: int, curr: list[int], currSum: int, res: list[list[int]]):
    if currSum == target:
        curr.sort()
        if curr not in res:
            res.append([*curr]) 
        return
    
    if idx == len(nums):
        return

    curr.append(nums[idx])
    currSum += nums[idx]
    backtrack(nums, target, idx+1, curr, currSum, res)
    currSum -= curr.pop()
    
    backtrack(nums, target, idx+1, curr, currSum, res)


def main():
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))

if __name__ == '__main__':
    main()