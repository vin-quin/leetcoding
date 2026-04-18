# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: int) -> int:
        from collections import defaultdict

        # The window length - most freq char in the window must be <= k for the window to be valid
        # Else we need to shift
        l, r = 0, 0
        maxWindow = 0
        freq = defaultdict(int)

        while r < len(s):
            freq[s[r]] += 1
            mostFreq = max(freq.values())
            # print(freq, mostFreq)

            # We assume the window is valid unless proven otherwise
            while r-l+1 - mostFreq > k: # We have more diff chars than replacements, this window is invalid
                freq[s[l]] -= 1 # Remove from window
                l += 1 # Shrink window until we are valid again
            
            if r-l+1 > maxWindow:
                maxWindow = r-l+1

            r += 1

        # print(maxWindow)
        return maxWindow

def main():
    s = Solution()
    print(s.solve("BABB", 1), 4)
    print(s.solve("ABAB", 2), 4)
    print(s.solve("ABABBA", 2), 5)
    print(s.solve("AABABBA", 1), 4)
    print(s.solve("AABABBABB", 3), 8)
    print(s.solve("AAAB", 0), 3)


if __name__ == '__main__':
    main()