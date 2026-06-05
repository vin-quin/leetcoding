# https://leetcode.com/problems/combination-sum-ii/description/
# 
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        self.backtrack(candidates, [], res, target, 0)

        return res
    
    def backtrack(self, candidates: list[int], nums: list[int], res: list[list[int]], target: int, idx: int):
        v = sum(nums)

        if v == target:
            ns = sorted(nums)
            if ns not in res:
                res.append(ns)
            return 
        elif v > target: # abort this line
            return
        
        if idx >= len(candidates):
            return
        
        for i in range(idx, len(candidates)):
            # Pick a number
            nums.append(candidates[i])
            self.backtrack(candidates, nums, res, target, i+1)
            # Remove number
            nums.pop()

def main():
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    # print(s.combinationSum2([2,5,2,1,2], 5))

if __name__ == '__main__':
    main()