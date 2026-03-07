# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # graph
        # each letter is a node
        # to find longest substring we want to search the graph, invert djikstra algo?
        # Could literally run inverse djikstra on every char in the graph and its faster than naive
        abcxyaz
        tabcdefghijklmnopqrstuvwxyz1a23456789
        
def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

if __name__ == '__main__':
    main()