# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Greedy

        # thru each character in s
        # 2 pointers, one for start of substr one lookahead
        # add each c in substr to set, if c exists then we are done and save if new max
        
        # We cannot continue from lookahead pointer as we risk skipping the start ofa longer substring
        abcxyaz
        tabcdefghijklmnopqrstuvwxyz1a23456789
        
def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

if __name__ == '__main__':
    main()