# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def solve(self, s1: str, s2: str) -> bool:
        # Order doesn't matter, only adjacency does i.e. each char in S1 is adjacent in S2's permutation
        # S1 has a permutation in S2

        # Can start from ANY letter in S1 in S2's permutation
        from collections import defaultdict
        masterFreqs = defaultdict(int)

        for c in s1:
            masterFreqs[c] += 1

        # While window is valid we will continue to pull chars from the s1 freqs
        # If right hits a point that invalidates the window then we need to shrink until we are valid again just like longest repeating char in sequence

        l, r = 0, 0
        # print(freqs)

        windowFreqs = defaultdict(int)
        while r < len(s2):
            windowFreqs[s2[r]] += 1

            # Window is invalid its impossible so fast forward and reset window
            if s2[r] not in masterFreqs: 
                l = r+1
                r = l
                windowFreqs.clear()
                continue

            # Winow is invalid we cannot afford another s2[r] in this substring, shrink window
            while windowFreqs[s2[r]] > masterFreqs[s2[r]] and l <= r:
                windowFreqs[s2[l]] -= 1
                l += 1

            # Window may be valid
            if windowFreqs == masterFreqs:
                return True
            
            r += 1

        return False


def main():
    s = Solution()
    print(s.solve("hello", "ooolleoooleh"), False)
    print(s.solve("ab", "eidbaooo"), True)
    print(s.solve("ab", "eidboaoo"), False)
    print(s.solve("eidbaooo", "ab"), False)
    print(s.solve("abc", "ab"), False)
    print(s.solve("abc", "abc"), True)
    print(s.solve("ab", "abc"), True)
    print(s.solve("ab", "back"), True)

if __name__ == '__main__':
    main()