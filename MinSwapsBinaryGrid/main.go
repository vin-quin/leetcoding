package main

import (
	"fmt"
)

// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid

func minSwaps(grid [][]int) int {
	// Generate ideal grid state for size, then AND/OR them against actual grid to determine if they could be valid or not

	// Sum of row 0 can never be greater than 1
	// Sum of row 1 can never be greater than 2
	// Sum of row 2 can never be greater than 3
	// Sum of row 3 can never be greater than 4

	// So if I sum every row I can theoretically sort the row array and count how many moves are required ot make it valid if possible

	for _, row := range grid {
		fmt.Println(row)
	}

	rowSums := make([]int, len(grid))
	for i, row := range grid {
		rowSums[i] = sum(row)
	}

	fmt.Println(rowSums)

	swaps := bubbleSort(rowSums)
	fmt.Println(swaps)

	return swaps
}

func sum(n []int) int {
	res := 0

	for _, num := range n {
		res += num
	}

	return res
}

func bubbleSort(a []int) int {
	swaps := 0

	for i := 1; i < len(a); i++ {
		if a[i-1] <= a[i] {

			tmp := a[i-1]
			a[i-1] = a[i]
			a[i] = tmp

			swaps++
		}
	}

	return swaps
}

func main() {
	input := [][]int{{0, 0, 1}, {1, 1, 0}, {1, 0, 0}}
	minSwaps(input)
}
