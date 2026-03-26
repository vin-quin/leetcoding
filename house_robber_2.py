# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3: # Too short to be interesting
            return max(nums) 
        
        lastRobbedIdx = 0
        value = nums[0]
        numRobbed = 1
        maxRobbed = len(nums) // 2 # Circular
        print(f'{maxRobbed=}')
        
        for i in range(1, len(nums)): # Rollover to first entry again to check properly
            print(f'{i=}/{lastRobbedIdx=}/{value=}/{numRobbed=}')
            if (i - lastRobbedIdx) == 1 and nums[lastRobbedIdx] < nums[i] : # Adjacent 
                value -= nums[lastRobbedIdx]
                value += nums[i] # rob this instead
                print(f'Robbing {nums[i]} @ {i} instead of {nums[lastRobbedIdx]} @ {lastRobbedIdx}')
                lastRobbedIdx = i
            elif numRobbed < maxRobbed and (i - lastRobbedIdx) > 1: # Rob it cause we can
                value += nums[i]
                print(f'Robbing {nums[i]} @ {i}')
                lastRobbedIdx = i
                numRobbed += 1

        return value


def main():
    s = Solution()
    # print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))
    # print(s.rob([1,2,3]))
    # print(s.rob([1,3,1,3,100]))
    # print(s.rob([200,3,140,20,10]))
    # print(s.rob([1,2,3,1,1,2,3,1]))

if __name__ == '__main__':
    main()