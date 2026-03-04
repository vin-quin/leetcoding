# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False

def main():
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == '__main__':
    main()