# https://leetcode.com/problems/unique-3-digit-even-numbers/
class Solution:
    def solve(self, digits: list[int]) -> int:
        nums = set()
        self.backtrack(digits, 0, "", nums)

        return len(nums)

    def backtrack(self, digits, idx, seq, nums):
        if len(seq) == 3:
            if int(seq) % 2 == 0:
                nums.add(seq)
            else:
                seq = seq[:2]

        if idx >= len(digits):
            return
        
        for i in range(len(digits)):
            if i != idx:
                self.backtrack(digits, i, seq + str(digits[idx]), nums)

       


def main():
    s = Solution()
    print(s.solve([1,2,3,4]))

if __name__ == '__main__':
    main()