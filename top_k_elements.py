# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = {}
        # freqs = [0] * len(nums)

        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1

        print(freqs)
        elements = sorted(list(freqs.items()), key=lambda a: a[1], reverse=True)
        print(elements)
 
        return [x[0] for x in elements[:k]]

def main():
    s = Solution()
    # print(s.topKFrequent([1],1 ))
    # print(s.topKFrequent([1,1,1,2,2,3],2 ))
    print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))

if __name__ == '__main__':
    main()