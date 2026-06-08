# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def solve(self, nums: list[int]) -> int:
        best = nums[0]
        total = nums[0]

        # is it more vvaluable to restart at i or continue
        for num in nums[1:]:
            if total+num >= num: # capture
                total+=num
            else: #reset from here and take this max
                total=num

            best = max(best, total)

        return best

def main():
    s = Solution()
    # print(s.solve([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.solve([5,4,-1,7,8]))

if __name__ == '__main__':
    main()