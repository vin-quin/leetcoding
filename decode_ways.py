# https://leetcode.com/problems/decode-ways/description/
from string import ascii_uppercase

ALPHABET = {i + 1: letter for i, letter in enumerate(ascii_uppercase)}

class Solution:
    def numDecodings(self, s: str) -> int:
        # Leading zero -> fail
        if s[0] == '0':
            return 0
        
        

def main():
    s = Solution()
    print(s.numDecodings("12"))
    print(s.numDecodings("226"))
    print(s.numDecodings("06"))
    print(s.numDecodings("11106"))

if __name__ == '__main__':
    main()