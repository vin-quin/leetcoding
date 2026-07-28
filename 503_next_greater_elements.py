# https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def solve(self, nums: list[int]) -> list[int]:
        nexts = []

        for i in range(len(nums)):
            for j in range(i, i+len(nums)):
                if nums[j%len(nums)] > nums[i]:
                    nexts.append(nums[j%len(nums)])
                    break
            else: # If this loop finishes we never found a next greater
                nexts.append(-1)

        return nexts

def main():
    s = Solution()
    print(s.solve([1,2,1]))
    print(s.solve([1,2,3,4,3]))

if __name__ == '__main__':
    main()