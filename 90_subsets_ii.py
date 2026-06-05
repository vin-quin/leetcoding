# https://leetcode.com/problems/subsets-ii/description/
# 
class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        self.backtrack(nums, [], res, 0)
            
        return res

    def backtrack(self, nums: list[int], pwr: list[int], res: list[list[int]], idx: int):
        if idx >= len(nums): # done
            # res.append()
            return 
        
        for i in range(0, len(nums)):
            if i == idx:
                continue 
            
            if pwr not in res:
                res.append(pwr.copy())

            pwr.append(nums[i])
            
            if pwr not in res:
                res.append(pwr.copy())

            self.backtrack(nums, pwr, res, i+1)
            pwr.pop()


def main():
    s = Solution()
    print(s.solve([1,2,2]))

if __name__ == '__main__':
    main()