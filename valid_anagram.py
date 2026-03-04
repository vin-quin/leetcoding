# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 0
        
        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 0
        
        return d1 == d2

def main():
    s = Solution()
    print(s.isAnagram("rat", "cat"))

if __name__ == '__main__':
    main()