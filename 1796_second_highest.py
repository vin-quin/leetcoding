# https://leetcode.com/problems/second-largest-digit-in-a-string/
class Solution:
    def solve(self, s: str) -> int:
        nums = [-1, -1]

        for c in s:
            if not c.isdigit():
                continue

            if int(c) > nums[0]:
                nums[0], nums[1] = int(c), nums[0]
            elif int(c) > nums[1] and int(c) != nums[0]:
                nums[1] = int(c)

        return nums[1]

def main():
    s = Solution()
    print(s.solve("dfa12321afd"))
    print(s.solve("abc1111"))

if __name__ == '__main__':
    main()