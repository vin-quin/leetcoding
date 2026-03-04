# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Assign each num to an index, each index points to count in array
        # Then sort array and slice K results easy
        
        # 1. Can just run a normal dict count and call it a day
        idx = 0
        freqIndex = {}
        freqs = [0] * len(nums)

        for n in nums:
            if n in freqIndex:
                freqs[freqIndex[n]] += 1
            else:
                freqIndex[n] = idx
                freqs[freqIndex[n]] = 1
                idx += 1

        freqs = freqs[:idx]
        print(freqIndex)
        print(freqs)
        print(sorted(freqs, reverse=True))
 
        return freqs[:k]
        # 2. Maxheap
        # 3. Array indexed by value, each index increments #

def main():
    s = Solution()
    # print(s.topKFrequent([1],1 ))
    # print(s.topKFrequent([1,1,1,2,2,3],2 ))
    print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))

if __name__ == '__main__':
    main()