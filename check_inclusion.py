# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def solve(self, s1: str, s2: str) -> bool:
        # Order doesn't matter, only adjacency does i.e. each char in S1 is adjacent in S2's permutation
        # S1 has a permutation in S2

        # Can start from ANY letter in S1 in S2's permutation
        from collections import defaultdict
        freqs = defaultdict(int)

        for c in s1:
            freqs[c] += 1

        # While window is valid we will continue to pull chars from the s1 freqs
        # If right hits a point that invalidates the window then we need to shrink until we are valid again just like longest repeating char in sequence

        l, r = 0, 0
        # print(freqs)

        while r < len(s2):
            # Scan forward until we find a character we can start building a permutation from
            while l < len(s2) and s2[l] not in freqs:
                l += 1
            
            r = l # Scan from valid window start

            # If s[r] is in freqs and > 0 this we are still valid
            # Else We are invalid
            freqs[s2[r]] -= 1

            if s2[r] not in freqs or freqs[s2[r]] < 0: # Invalid window, shrink
                freqs[s2[l]] += 1 # We need this letter again for a valid permutation
                l += 1

            # print(sum(freqs.values()))
            if sum(freqs.values()) == 0: # A permutation has been found
                return True
            
            r += 1

        return False


def main():
    s = Solution()
    # print(s.solve("ab", "eidbaooo"), True)
    print(s.solve("ab", "eidboaoo"), False)
    # print(s.solve("eidbaooo", "ab"), False)
    # print(s.solve("abc", "ab"), False)
    # print(s.solve("abc", "abc"), True)
    # print(s.solve("ab", "abc"), True)
    # print(s.solve("ab", "back"), True)

if __name__ == '__main__':
    main()