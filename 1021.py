# https://leetcode.com/problems/remove-outermost-parentheses/   
class Solution:
    def solve(self, s: str) ->  str:
        stack = []
        ss = ""

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                j = stack.pop()

                if len(stack) == 0: # This was an outermost paren
                    ss += s[j+1:i]

        return ss

def main():
    s = Solution()
    print(s.solve("(()())(())"))
    print(s.solve("(()())(())(()(()))"))
    print(s.solve("()()"))

if __name__ == '__main__':
    main()