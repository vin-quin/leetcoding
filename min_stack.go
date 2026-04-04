package main

type MinStack struct {
	items [][]int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	sml := val
	if len(this.items) != 0 {
		sml = min(this.items[len(this.items)-1][1], val)
	}

	this.items = append(this.items, []int{val, sml})
}

func (this *MinStack) Pop() {
	this.items = this.items[:len(this.items)-1]
}

func (this *MinStack) Top() int {
	return this.items[len(this.items)-1][0]
}

func (this *MinStack) GetMin() int {
	return this.items[len(this.items)-1][1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
