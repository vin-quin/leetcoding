# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        
        if str1 + str2 != str2 + str1:
            return ""

        g = gcd(len(str1), len(str2))
        return str1[:g]


def main():
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))

if __name__ == '__main__':
    main()