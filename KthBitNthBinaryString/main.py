# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        print(self.generate(2))
        
    def generate(self, n: int):
        if n <= 1:
            return (b'0')
        
        prev = self.generate(n-1)
        print((prev))
        print(self.bit_not(int(prev), len(prev)))
        return prev + b'1' + self.bit_not(int(prev), len(prev)).to_bytes()
    
    def bit_not(self, n, numbits=8):
        return (1 << numbits) - 1 - n

def main():
    s = Solution()
    s.findKthBit(3, 1)

if __name__ == '__main__':
    main()

