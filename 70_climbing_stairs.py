# https://leetcode.com/problems/climbing-stairs/description/
# 
class Solution:
    def solve(self, n: int) -> int:       
        ways = [1,2]

        for i in range(2, n):
            ways.append(ways[i-2] + ways[i-1])
        
        return ways[-1]
        
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