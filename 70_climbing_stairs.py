# https://leetcode.com/problems/climbing-stairs/description/
# 
class Solution:
    def solve(self, n: int) -> int:
        return rec(n)
        
def rec(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return rec(n-2) + rec(n-1)

def main():
    s = Solution()
    print(s.solve(2))

if __name__ == '__main__':
    main()