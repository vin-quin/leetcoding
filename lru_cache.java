// https://leetcode.com/problems/lru-cache/
import java.util.HashMap;
class Node {
    public int key;
    public int val;
    public Node next;
    public Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    private HashMap<Integer, Node> kv; // Key:Node 
    private Node head;
    private Node tail;
    private int capacity; 

    // Doubly Linked List w/ HashMap - Head should always be oldest
    public LRUCache(int capacity) {
        this.kv = new HashMap<>(capacity);
        this.capacity = capacity;
        this.head = new Node(-1, -1);

        Node curr = this.head;
        for (int i = 0; i<capacity-1; i++) { // Already have 1 node
            Node tmp = curr;
            curr.next = new Node(-1, -1);
            curr = curr.next;
            curr.prev = tmp;
        }

        this.tail = curr;
    }
    
    // Pop key from DLL and make it the new tail
    public int get(int key) {
        Node v = this.kv.get(key);
        if (v != null) {
            // Remove key wherever it was prior
            Node prev = v.prev;
            Node next = v.next;
            prev.next = next;
            next.prev = prev;
            
            // Update as youngest accessed
            // this.tail.next = new Node(v.val);
            // this.tail.next.prev = this.tail;
            // this.tail = this.tail.next;
            // this.kv.put(key, this.tail);
            this.updateTail(key, v.val);

            return v.val;
        }


        System.out.println("DEBUG GET");
        System.out.println(kv);
        Node curr = this.head;
        while (curr != null){
            System.out.printf("Key: %d, Val: %d, Prev: %s, Next: %s", curr.key, curr.val, curr.prev, curr.next);
        }

        return -1;
    }
    
    // If at capacity, delete head and set new kv to tail
    public void put(int key, int value) {
        if (this.kv.size() == this.capacity) { // We have no available cache, remove oldest
            // Head is oldest so delete that entry then update tail as normal
            Node oldest = this.head;
            this.head = this.head.next;
            this.head.prev = null;
            this.kv.remove(oldest.key);
        }

        this.updateTail(key, value);
    }   

    private void updateTail(int key, int val) {
        this.tail.next = new Node(key, val);
        this.tail.next.prev = this.tail;
        this.tail = this.tail.next;
        this.kv.put(key, this.tail);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */