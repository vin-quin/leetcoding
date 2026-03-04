# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupFreqs = []
        groups = []

        if len(strs) == 0: 
            return [[""]]

        for i in range(0, len(strs)):
            freq = {}
            for c in strs[i]:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1

            # if this freq already in groups, its not new so find where it belongs
            try:
                idx = groupFreqs.index(freq)
                groups[idx] =  [*groups[idx], strs[i]]
            # else its new
            except ValueError:
                groupFreqs.append(freq)
                groups.append([strs[i]])
        
        return groups

def main():
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == '__main__':
    main()