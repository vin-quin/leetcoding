# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: str) -> int:
        ...


def main():
    s = Solution()
    print(s.solve("ABAB", 2))
    print(s.solve("AABABBA", 1))

if __name__ == '__main__':
    main()