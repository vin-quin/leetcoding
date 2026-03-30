# https://leetcode.com/problems/decode-ways/description/
MAPPING = { str(i+1): chr(i + ord('A')) for i in range(26)}

class Solution:
    def solve(self, s: str) -> int:
        curr, prev = None, None

        for i in range(len(s)):
            prev = curr
            curr = s[i]

            



def main():
    s = Solution()
    print(s.solve("12"))
    # print(s.solve("226"))
    # print(s.solve("06"))
    # print(s.solve("11106"))

if __name__ == '__main__':
    main()