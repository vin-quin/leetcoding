// https://leetcode.com/problems/lru-cache/
class Node {
    public int key;
    public int val;
    public Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
    }

}
class LRUCache {
    private Node head;
    private Node lru; 

    public LRUCache(int capacity) {
        this.head = new Node();
        this.lru = head;
        Node curr = this.head;

        for (int i = 0; i<capacity-1; i++) { // Already have 1 node
            curr.next = new Node();
            curr = curr.next;
        }
    }
    
    public int get(int key) {
        Node curr = this.head;

        while (curr != null) {
            if (curr.key == key) {
                return curr.val;
            }

            curr = curr.next;
        }

        return -1;
    }
    
    public void put(int key, int value) {
        // We place in this.lru then step it forward for next. Cycle to head on null
        if (this.lru == null) {
            this.lru = this.head;
        }

        this.lru.val
    }   
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */