# https://leetcode.com/problems/decode-ways/description/
ALPHABET = {
    "1": 'A', "2": 'B', "3": 'C', "4": 'D', "5": 'E', "6": 'F', "7": 'G', "8": 'H', "9": 'I',
    "10": 'J', "11": 'K', "12": 'L', "13": 'M', "14": 'N', "15": 'O', "16": 'P', "17": 'Q',
    "18": 'R', "19": 'S', "20": 'T', "21": 'U', "22": 'V', "23": 'W', "24": 'X', "25": 'Y', "26": 'Z'
}
MAX_N = len(ALPHABET) #

class Solution:
    def numDecodings(self, s: str) -> int:
        # Leading zero -> fail
        if s[0] == '0':
            return 0
        
        strs = []

        # if int(s[:2]) <= MAX_N: # Decodeable, else needs to be treated as individual chars
        #     strs.append(ALPHABET[s[:2]])

        count = 1
        prev = s[0]
        print(f'Init: {count}')
        
        for i in range(1, len(s)):
            if prev == "0": # No leading zeroes allowed
                continue

            if i+1 < len(s) and s[i+1] == "0": # We lose 1 possibility with a trailing zero so just continue
                continue
            # suffix1 = ALPHABET[s[i]]
            # suffix2 = None
            if int(prev + s[i]) <= MAX_N:
                count += 1 # Must double because each possible string now has 2 new paths

            # if int(prev + s[i]) <= MAX_N: # This branches to another possible encoding
            #     suffix2 = ALPHABET[prev + s[i]]

            # for j in range(len(strs)):
            #     orig = strs[j]

            #     print(f'Updating str: {orig} with {suffix1}')
            #     strs[j] += suffix1

                # if suffix2:
                #     print(f'New str: {orig} with {suffix2}')
                #     strs.append(orig + suffix2)

            prev = s[i]

        return count


def main():
    s = Solution()
    print(s.numDecodings("10"))
    # print(s.numDecodings("12"))
    # print(s.numDecodings("226"))
    # print(s.numDecodings("06"))
    # print(s.numDecodings("11106"))

if __name__ == '__main__':
    main()