# https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def solve(self, s: str, t: str) -> str:
        # Smallest window where ALL charactes of t (incl. dupes) exist in s
        # No guarantee that this window will exist in s

        from collections import Counter

        window = s + '-' # Invalid char just so we know the window hasn't been modified
        freqT = Counter(t)
        # print(freqT)

        #  Expand while winow is invalid and r < length
            # If window is valid
            #     Save if smallest window then
            #     Shrink until invalid

        l, r = 0, 0
        windowFreq = freqT # Once each value is <=0 the window is valid

        while l <= r < len(s):
            # print(f'{s[l:r+1]}, {l=}, {r=}, {window=}, {windowFreq=}')
            # A window is invalid if sum of freqT > sum of windowFreq for eahc letter in freqT
            # This meanss not enough letters from t in the window exist to be a valid substring
            # We don't want to muddy our freq with chars not common to both strings
            if s[r] in windowFreq:
                windowFreq[s[r]] -= 1

            # Max prevents ufixes issue where sum would be 0 from seeing multiple dupe letters but not ALL the required letters
            while max(windowFreq.values()) <= 0 and l <= r: # Window is valid now
                # print('Window is valid', windowFreq)
                if len(s[l:r+1]) <= len(window): # New smallest substring
                    # print('Replacing')
                    window = s[l:r+1]
                
                if s[l] in windowFreq:
                    windowFreq[s[l]] += 1
                l += 1
            
            # Bounds safe increment
            r = min(len(s), r+1)

        return window if len(window) <= len(s) else '' # No valid substring t in s


def main():
    s = Solution()
    print(s.solve("aaaaaaaaaaaabbbbbcdd", "abcdd"), 'abbbbbcdd')
    print(s.solve("ADOBECODEBANC", "ABC"), 'BANC')
    print(s.solve("ADOBECODEBANC", "DEDOB"), 'DOBECOD')
    print(s.solve("a", "a"), 'a')
    print(s.solve("a", "aa"), '')

if __name__ == '__main__':
    main()