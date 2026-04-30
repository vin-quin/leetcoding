// https://leetcode.com/problems/implement-stack-using-queues/description/
class MyStack {
    private ArrayDeque<Integer> q;

    public MyStack() {
        this.q = new ArrayDeque<Integer>();
    }
    
    public void push(int x) {
        this.q.addFirst(x);
    }
    
    public int pop() {
        return this.q.pollFirst();
    }
    
    public int top() {
        return this.q.peekFirst();
    }
    
    public boolean empty() {
        return this.q.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */