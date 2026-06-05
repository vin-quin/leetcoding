# https://leetcode.com/problems/subsets-ii/description/
# 
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            self.backtrack(nums, [], res, i)
            
        return res

    def backtrack(self, nums: list[int], pwr: list[int], res: list[list[int]], idx: int):
        if idx >= len(nums): # done
            # res.append()
            return 
        
        if pwr not in res:
            res.append(pwr.copy())
        pwr.append(nums[idx])
        
        if pwr not in res:
            res.append(pwr.copy())

        self.backtrack(nums, pwr, res, idx+1)
        pwr.pop()


def main():
    s = Solution()
    print(s.solve([1,2,2]))

if __name__ == '__main__':
    main()