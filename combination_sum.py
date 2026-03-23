# https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Any candidate > target can be skipped
        candidates.sort()
        print(candidates)

        perms = []
        rec(candidates, [], target, perms)

        return [p for p in perms if p is not None]


def rec(candidates: list[int], perm:list[int], t: int, perms=[]):
    if t < 0:
        return None # No valid perm
    
    if t == 0:
        return perm
    
    # perms = []

    for i in range(len(candidates)):
        perms.append(rec(candidates[i:], [*perm, candidates[i]], t-candidates[i], perms))

    # return perms


def main():
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))

if __name__ == '__main__':
    main()