# https://leetcode.com/problems/task-scheduler/description/
import heapq
class Solution:
    def solve(self, tasks: list[str], n: int) -> int:
        # If we only have tasks "A"*4 and n=2, we must idle twice after processing each A before processing the next
        freqs = {}
        q = []
        chain = []

        for t in tasks:
            if t in freqs:
                freqs[t] += n+1
            else:
                freqs[t] = 0

            heapq.heappush(q, [freqs[t], t])

        # print(freqs)
        # print(q)

        cnt = 0
        # Get the min from the q
        while q:
            v = heapq.heappop(q)

            if v[0] <= cnt: # if minQ <= cnt we can add to chain
                chain.append(v[1])
            else: # else we need to insert an idle
                chain.append("IDLE")
                heapq.heappush(q, v)

            cnt += 1

        # print(chain)
        return len(chain)

def main():
    s = Solution()
    print(s.solve(["A","A","A","B","B","B"], 2))

if __name__ == '__main__':
    main()