# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        print(freq)
        common = max(freq.items(), key=lambda x: x[1])
        print(common)

        longest = ""

        idx = 0
        while idx < len(s):
            substring = ""
            replacements = k

            for i in range(idx, len(s)):
                if s[i] != common[0]:
                    if replacements > 0: 
                        replacements -= 1
                    else:
                        break

                substring += common[0]

            if len(substring) > len(longest):
                longest = substring

            idx += 1

        print(longest)
        return len(longest)



def main():
    s = Solution()
    print(s.solve("ABAB", 2))
    print(s.solve("AABABBA", 1))
    print(s.solve("AABABBABB", 3))

if __name__ == '__main__':
    main()