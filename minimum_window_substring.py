# https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def solve(self, s: str, t: str) -> str:
        # Smallest window where ALL charactes of t (incl. dupes) exist in s
        # No guarantee that this window will exist in s

        from collections import Counter

        window = ''
        freqT = Counter(t)
        print(freqT)

        #  Expand while winow is invalid and r < length
            # If window is valid
            #     Save if smallest window then
            #     Shrink until invalid

        l, r = 0, len(s)-1
        windowTargetFreq = freqT # Number of letters still needed in the window

        # Shrink the window, we begin ASSUMING the entire string S is a valid window
        while l < r:
            # If both L and R are chars that occur in T then we will arbitrarily choose to shrink L
            #     (May need ot check which side to shrink keeps validity to pick)

            # If only L is in T we will shrink R
            if s[l] in freqT:
                r -= 1
            # If only R is in T we will shrink L
            elif s[r] in freqT:
                l += 1
            # Else neither are in and we will shrink BOTH
            else:
                l += 1
                r -= 1

            # If windowFreq >= freqT
            #     This is a valid window, set it if smaller than current window        


        return window if window != s else '' # No valid substring t in s


def main():
    s = Solution()
    print(s.solve("ADOBECODEBANC", "ABC"))

if __name__ == '__main__':
    main()