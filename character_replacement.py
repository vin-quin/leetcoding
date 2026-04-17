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
        replaceChar = max(freq)
        replacementsLeft = k
        maxLen = 0

        while r < len(s):
            if s[r] == replaceChar: # Char already correct keep searching
                if maxLen < (r-l)+1:
                    maxLen = (r-l)+1

                r += 1

                continue

            # Char needs to be replaced
            if replacementsLeft > 0:
                replacementsLeft -= 1

                if maxLen < (r-l)+1:
                    maxLen = (r-l)+1

                r += 1 # Char has been replaced

            else: # Cant replace anymore tail has to shrink 
                while s[l] == replaceChar: # Inch up until we found a char we replaced, go past it to recover 1 replacement
                    l += 1
                l += 1 # So it continues AFTER the replacement
                replacementsLeft += 1

        return maxLen

def main():
    s = Solution()
    print(s.solve("ABAB", 2), 4)
    print(s.solve("ABABBA", 2), 5)
    print(s.solve("AABABBA", 1), 4)
    print(s.solve("AABABBABB", 3), 8)

if __name__ == '__main__':
    main()