# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
class Solution:
    def solve(self, nums: list[int], k :int) -> int:
        nums.sort()
        target = k

        for n in nums:
            if n == target:
                target += k
        
        return target


def main():
    s = Solution()
    print(s.solve([8,2,3,4,6], 2))

if __name__ == '__main__':
    main()