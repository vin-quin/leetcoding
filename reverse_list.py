# https://leetcode.com/problems/reverse-linked-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        stack = []

        node = head
        while node:
            stack.append(node)
            node = node.next

        print(stack)
        n = stack.pop()

        while stack:
            nextN = stack.pop()

            n.next = nextN
            n = nextN

        return n

def rec(head: Optional[ListNode]):
    if head:
        n = rec(head.next)
        return n
    
    head.next = rec(head.next)

    return head

def iter(head: Optional[ListNode]):
    if not head:
            return head
        
    stack = [None]

    node = head
    while node:
        stack.append(node)
        node = node.next

    head = stack.pop()
    node = head

    while stack:
        node.next = stack.pop()
        node = node.next

    return head


def main():
    s = Solution()
    print(s.solve(ListNode(1, ListNode(2))))

if __name__ == '__main__':
    main()