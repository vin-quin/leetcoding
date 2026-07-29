# https://leetcode.com/problems/rotate-string/
class Solution:
    def solve(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        attempts = 0

        while s != goal and attempts != len(s):
            s = s[1:] + s[0]
            attempts += 1

        return s == goal

def main():
    s = Solution()
    print(s.solve("abcde", "cdeab"))
    print(s.solve("abcde", "abced"))

if __name__ == '__main__':
    main()