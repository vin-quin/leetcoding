# https://leetcode.com/problems/jump-game/description/
# 
class Solution:
    def solve(self, nums: list[int]) -> bool:
        # Just take the biggest jump possible nad rollback if we cant
        pos = 0
        
        while pos != len(nums)-1:
            for i in range(nums[pos], 0, -1):
                

        return True

def jump(nums: list[int], idx: int) -> bool:
    if idx >= len(nums): #overshot
        return False
    
    if idx == len(nums)-1: # We hit the end
        return True 
    
    for i in range(nums[idx], 0, -1): #. try progessively smaller jumps
        r = jump(nums, idx+i)
        
        if r: # quit early on success
            return True
    
    return False
        

def main():
    s = Solution()
    print(s.solve([2,3,1,1,4]))

if __name__ == '__main__':
    main()