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

        for l in range(len(s2)):
            # print(f'Starting @ {l}')
            freqs = masterFreqs
            r = l
            while r < len(s2) and s2[l] in freqs: # Valid window start
                # print(f'Scan {l=} - {r=}')

                if s2[r] not in freqs: # Unfixable invalid
                    freqs[s2[l]] += 1
                    break

                freqs[s2[r]] -= 1
                if freqs[s2[r]] < 0: # Window is invalid shrink it until it is
                    freqs[s2[l]] += 1
                    l += 1
                print(freqs)
                if sum(freqs.values()) == 0:
                    return True

                r += 1



        # while r < len(s2):
            # If R is not in S1 then scna forward until it is and we begin from
            
            # # Scan forward until we find a character we can start building a permutation from
            # while l < len(s2) and s2[l] not in freqs:
            #     l += 1
            #     r = l # Scan from valid window start if we need to move forward
            # print(l, r)

            # # If s[r] is in freqs and > 0 this we are still valid
            # # Else We are invalid
            # freqs[s2[r]] -= 1

            # if s2[r] not in freqs or freqs[s2[r]] < 0: # Invalid window, shrink
            #     print('shrinking')
            #     freqs[s2[l]] += 1 # We need this letter again for a valid permutation
            #     l += 1

            # print(freqs)
            # if r-l+1 == targetSum: # A permutation has been found
            #     return True
            
            # r += 1

        return False


def main():
    s = Solution()
    print(s.solve("hello", "ooolleoooleh"), False)
    # print(s.solve("ab", "eidbaooo"), True)
    # print(s.solve("ab", "eidboaoo"), False)
    # print(s.solve("eidbaooo", "ab"), False)
    # print(s.solve("abc", "ab"), False)
    # print(s.solve("abc", "abc"), True)
    # print(s.solve("ab", "abc"), True)
    # print(s.solve("ab", "back"), True)

if __name__ == '__main__':
    main()