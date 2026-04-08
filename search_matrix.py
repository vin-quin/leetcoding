# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def solve(self, matrix: list[list[int]], target: int) -> bool:
        # Binary search each row and then once a row is determined binary search that row
        row = searchRow(matrix, target, 0, len(matrix)-1)
        r = binarySearch(row, target, 0, len(row)-1)
        print(row)
        print(r)
        return  r != -1 

# Narrows it down to 1 or 2 rows the value could be in
def searchRow(matrix: list[list[int]], target: int, l: int, r: int) -> list[int]:
    if l > r:
        return []
    
    mid = l+(r-l) // 2

    if target < matrix[mid][0]: # Target is below the first value at mid so go left
        return searchRow(matrix, target, l, mid-1)
    elif target > matrix[mid][-1]: # Target greater than biggest element in mid array so go right
        return searchRow(matrix, target, mid+1, r)
    else: # The target is in the mid array or not at all
        return matrix[mid]
    
def binarySearch(arr: list[int], target: int, l: int, r: int) -> int:
    if l > r or not arr:
        return -1
    
    mid = l+(r-l) // 2
    if arr[mid] == target:
        return mid
    
    if target < arr[mid]: # Target is below the first value at mid so go left
        return binarySearch(arr, target, l, mid-1)
    elif target > arr[mid]: # Target greater than biggest element in mid array so go right
        return binarySearch(arr, target, mid+1, r)

def main():
    s = Solution()
    print(s.solve([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.solve([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 8))
    print(s.solve([[1]], 2))
    print(s.solve([[1]], 1))

if __name__ == '__main__':
    main()