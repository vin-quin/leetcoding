# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: list[int]) -> int:
        n1, n2 = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                n1 += nums[i]
            else:
                n2 += nums[i]

        if len(nums) % 2 != 0:
            n1 -= nums[-1]
        print(f'{n1=}, {n2=}')
        return max(n1, n2)

def main():
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))
    print(s.rob([1,3,1,3,100]))

if __name__ == '__main__':
    main()