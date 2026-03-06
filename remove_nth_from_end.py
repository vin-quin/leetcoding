# https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=blind75
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'[{self.val}]'

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Sliding window of last N+1 nodes, so when we reach the end we can still reference the Nth's prev node and update the connection
        window = [] 
        curr = head

        while curr != None:
            window.append(curr)
            curr = curr.next

        # Curr=end so window's most recent value is end, sub n indices to get element to pop
        rIdx = len(window)-n
        if rIdx == 0: # Remve head
            return head.next
        
        predecessor = window[rIdx-1]

        if rIdx == len(window)-1: # Remove tail
            successor = None
        else:
            successor = window[rIdx+1]

        predecessor.next = successor

        return head

def main():
    s = Solution()
    print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))), 1))
    # print(s.removeNthFromEnd(ListNode(1, ListNode(2, None)), 2))

if __name__ == '__main__':
    main()