# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""

        for i in range(len(s)):
            # Assume odd
            l, r = i, i
            while l >= 0 and r  < len(s) and s[l] == s[r]:
                if (r-l+1) > len(palindrome):
                    palindrome = s[l:r+1]
                l -= 1
                r += 1

            # Assume event
            l, r = i, i+1
            while l >= 0 and r  < len(s) and s[l] == s[r]:
                if (r-l+1) > len(palindrome):
                    palindrome = s[l:r+1]
                l -= 1
                r += 1

        return palindrome

s = Solution()
print(s.longestPalindrome("babad"))