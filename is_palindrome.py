# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def solve(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True


def main():
    s = Solution()
    # print(s.solve("A man, a plan, a canal: Panama"))
    # print(s.solve("race a car"))
    # print(s.solve("racecar"))
    # print(s.solve(" "))
    print(s.solve("0P"))

if __name__ == '__main__':
    main()