# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/
class Solution:
    def solve(self, n: str) -> int:
        steps = 0

        for d in n:
            steps = max(steps, int(d))
            if steps == 9:
                return steps
        
        return steps

def main():
    s = Solution()
    print(s.solve("32"))
    print(s.solve("82734"))
    print(s.solve("27346209830709182346"))

if __name__ == '__main__':
    main()