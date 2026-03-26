# https://leetcode.com/problems/clone-graph/description/
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        print(node)

def main():
    s = Solution()
    root = Node(1)
    
    print(s.cloneGraph([Node(1, [2,4]),Node(2, [1,3]),Mode(3, [2,4]),Node(4, [1,3])]))
    # print(s.cloneGraph([[]]))
    # print(s.cloneGraph([]))

if __name__ == '__main__':
    main()