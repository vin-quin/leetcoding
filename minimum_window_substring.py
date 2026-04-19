# https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def solve(self, s: str, t: str) -> str:
        # Smallest window where ALL charactes of t (incl. dupes) exist in s
        # No guarantee that this window will exist in s

        from collections import Counter

        window = ''
        freqT = Counter(t)
        print(freqT)

        l, r = 0, len(s)-1

        # Shrink the window, we begin ASSUMING the entire string S is a valid window
        while l < r:
            # If both L and R are chars that occur in T then we will arbitrarily choose to shrink L
            #     (May need ot check which side to shrink keeps validity to pick)
            # If only L is in T we will shrink R
            # If only R is in T we will shrink L
            # Else neither are in and we will shrink BOTH

            # If windowFreq >= freqT
            #     This is a valid window, set it if smaller than current window        


        return window if window != s else '' # No valid substring t in s


def main():
    s = Solution()
    print(s.solve("ADOBECODEBANC", "ABC"))

if __name__ == '__main__':
    main()