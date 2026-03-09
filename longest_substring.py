# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        freqs = {} # Map of freqs for each substr, when a freq for a substr > 1 it needs to be reset
        longest = 0
        for c in s:
            print(f'LETTER: {c}')
            if c not in freqs:
                freqs[c] = {c: 0}
                print(f'Starting new subtr: {c}')

            keyRemovals = []
            for k in freqs: 
                if c not in freqs[k]:
                    freqs[k][c] = 1
                else:
                    freqs[k][c] += 1

                subFreq = freqs[k][c]

                if subFreq > 1: # Repeated char
                    # Do longest check and reset
                    chrLength = sum(freqs[k].values())-1 # Sub 1 as we have added a repeating character to the count
                    print(f'Length Check: {chrLength=}, {freqs[k]}')
                    if  chrLength > longest:
                        print(f'New longest is: {chrLength} - {freqs[k]}')
                        longest = chrLength

                    print(f'Resetting substr for {c}')
                    freqs[k].clear()
                    freqs[k][c] = 1
            
            print(f'{freqs=}')

        for k in freqs: # Final pass required for end of string with unterminated substrings
            chrLength = sum(freqs[k].values()) # No Sub 1 as duplicate wouldve been counted in main flow
            print(f'Final Length Check: {chrLength=}, {freqs[k]}')
            if  chrLength > longest:
                print(f'Final New longest is: {chrLength} - {freqs[k]}')
                longest = chrLength

        return longest


def main():
    s = Solution()
    # print(s.lengthOfLongestSubstring("pwwkew"))
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("bbbb"))
    # print(s.lengthOfLongestSubstring("aab"))
    print(s.lengthOfLongestSubstring("nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))

if __name__ == '__main__':
    main()