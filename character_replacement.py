# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # Replace each char in string with the most freq occurring char while we can.
        # Kinda like a worm, keep inching forwards til you find an unreplaceable
        # Then inch your tail back up until you can replace again. Repeat to EOF
        l, r = 0, 0
        replaceChar = max(freq.items(), key=lambda x: x[1])[0]
        replacementsLeft = k
        maxLen = 0

        # while window is valid extend to the right if possible
        #     if window is invalidated
        #         Check if we beat previous best size
        #         shrink L->R until valid

        while r < len(s):
            if s[r] == replaceChar: # Char already correct keep searching
                r += 1

                continue

            # Char needs to be replaced
            if replacementsLeft > 0:
                replacementsLeft -= 1
                r += 1 # Char has been replaced
                
                continue

            # Window is invalid at this point, we can check
            if maxLen < (r-l)+1:
                maxLen = (r-l)+min(l, 1)

            # Cant replace anymore tail has to shrink 
            while s[l] == replaceChar and l < r: # Inch up until we found a char we replaced, go past it to recover 1 replacement
                l += 1
            l += 1 # So it continues AFTER the replacement
            r += 1 # Go next, we just replaced the oldest with newest so we can continue
            replacementsLeft += min(k, 1) # If k==0 we dont want to increment wrongly

        return max(maxLen, ((r-1)-l+1))

def main():
    s = Solution()
    print(s.solve("ABAB", 2), 4)
    print(s.solve("ABABBA", 2), 5)
    print(s.solve("AABABBA", 1), 4)
    print(s.solve("AABABBABB", 3), 8)
    print(s.solve("AAAB", 0), 3)


if __name__ == '__main__':
    main()