# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:

        def get_max(nums):
            prev_rob = max_rob = 0

            for cur_val in nums:
                temp = max(max_rob, prev_rob + cur_val)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob
        
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])


def main():
    s = Solution()
    # print(s.rob([2,3,2]))
    # print(s.rob([1,2,3,1]))
    # print(s.rob([1,2,3]))
    print(s.rob([1,3,1,3,100]))
    # print(s.rob([200,3,140,20,10]))
    # print(s.rob([1,2,3,1,1,2,3,1]))

if __name__ == '__main__':
    main()