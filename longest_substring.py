# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # graph
        # each letter is a node
        # to find longest substring we want to search the graph, invert djikstra algo?
        # Could literally run inverse djikstra on every char in the graph and its faster than naive
        # abcxyaz
        # tabcdefghijklmwnopqrstuvwxyz1a2345q6789
        # For each character in str
        # Build all substring in a hashmap we go so for abcabcbb
        # {
        #   a: abc,
        #   b: bc,
        #   c: c,
        # }
        # When seeing an existing character in the str, we end the current substr for that letter, save, and start again
        # This means we're iterating of n_s entries per char at most, up to ~100 at worst so O(N*M)?

        strs = {}
        longest = 1
        for c in s:

            if c in strs:
                print(f'{c} in strs, removing...')
                str = strs.pop(c)
            else:
                strs[c] = c
                print(f'Updating strs: {strs}')

            for k in strs:
                if k == c:
                    continue 

                strs[k] += c
                if len(strs[k]) > longest:
                    longest = len(strs[k]) # We always append first so dont count repeated char we added
                    # longest = strs[k]
                    print(f'New longest is: {strs[k]}')

            # print(f'Char: {c}')
            # print(f'Strs: {strs}')

        return longest


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))

if __name__ == '__main__':
    main()