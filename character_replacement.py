# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def solve(self, s: str, k: int) -> int:
        from collections import defaultdict

        # freq = defaultdict(int)
        # for c in s:
        #     freq[c] += 1

        # print(freq)
        # common = max(freq.items(), key=lambda x: x[1])
        # print(common)

        # longest = ""
        # l, r = 0, 1 # Expand window until we bazinga
        # while r < len(s):
        #     if (r-l)-common[1] <= k:
        #         r +=1
        #     else:
        #         l +=1


        l, r = 0, 0
        while r < len(s):
            window = s[l:r+1]
            # print(window)

            freq = defaultdict(int)
            for c in window:
                freq[c] += 1
            # print(freq)

            if len(window)-max(freq.items(), key=lambda x: x[1])[1] <= k:
                r +=1
            else:
                l +=1

        return len(window)



def main():
    s = Solution()
    print(s.solve("ABAB", 2))
    print(s.solve("ABABBA", 2))
    print(s.solve("AABABBA", 1))
    print(s.solve("AABABBABB", 3))

if __name__ == '__main__':
    main()