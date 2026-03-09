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
        
        strs = [
            ALPHABET[s[0]],
        ]

        # if int(s[:2]) <= MAX_N: # Decodeable, else needs to be treated as individual chars
        #     strs.append(ALPHABET[s[:2]])

        print(f'Init: {strs}')
        prev = s[0]
        for i in range(0, len(s)):
            suffix1 = ALPHABET[s[i]]
            suffix2 = None

            if int(prev + s[i]) <= MAX_N: # This branches to another possible encoding
                suffix2 = ALPHABET[prev + s[i]]

            for j in range(len(strs)):
                orig = strs[j]

                print(f'Updating str: {orig} with {suffix1}')
                strs[j] += suffix1

                if suffix2:
                    print(f'New str: {orig} with {suffix2}')
                    strs.append(orig + suffix2)

            prev = s[i]

        print(f'{strs}')


def main():
    s = Solution()
    # print(s.numDecodings("12"))
    print(s.numDecodings("226"))
    # print(s.numDecodings("06"))
    # print(s.numDecodings("11106"))

if __name__ == '__main__':
    main()