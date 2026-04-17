# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: int) -> int:
        from collections import defaultdict

        l, r = 0, 0
        replacementsLeft = k
        maxLen = 0

        # The window length - most freq char in the window must be <= k for the window to be valid
        # Else we need to shift
        window = ''
        maxWindow = ''
        freq = defaultdict(int)

        while r < len(s):
            freq[r] += 1
            mostFreq = max(freq.items(), key=lambda x: x[1])

            if s[r] == mostFreq[0]: # This is our targetChar we just expand
                r += 1
                continue

            if len(s[l:r+1]) > len(maxWindow):
                maxWindow = s[l:r+1]

            while len(window[l:r+1]) - mostFreq[1] > k: # We have more diff chars than replacements, this window is invalid
                freq[l] -= 1 # Remove from window
                l += 1 # Shrink window until we are valid again

            r += 1

        print(maxWindow)
        return len(maxWindow)

def main():
    s = Solution()
    # print(s.solve("ABAB", 2), 4)
    print(s.solve("ABABBA", 2), 5)
    # print(s.solve("AABABBA", 1), 4)
    # print(s.solve("AABABBABB", 3), 8)
    # print(s.solve("AAAB", 0), 3)


if __name__ == '__main__':
    main()