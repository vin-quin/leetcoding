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
    private HashMap<Integer, Node> kv;
    private Node head;
    private Node tail;
    private int capacity;

    public LRUCache(int capacity) {
        this.kv = new HashMap<>(capacity);
        this.capacity = capacity;
        this.head = new Node(Integer.MIN_VALUE, Integer.MIN_VALUE);
    }

    public int get(int key) {
        Node v = this.kv.get(key);

        if (v != null) {
            // Remove v from the list
            this.remove(v);

            // Append at the end
            this.append(v);

            return v.val;
        }

        return -1;
    }

    public void put(int key, int value) {
        // Key already in just update the value
        Node v = this.kv.get(key);
        if (v != null) {
            v.val = value;
            return;
        }

        Node entry = new Node(key, value);
        if (this.kv.size() == this.capacity) { // Need to replace
            Node oldest = this.head.next; // Skip dummy
            this.kv.remove(oldest.key);

            // Replace head with new oldest
            this.head.next = oldest.next;
            this.head.next.prev = oldest.prev;
        }

        // Can just add
        if (this.head == null) {
            this.head = entry;
            this.tail = entry;
        } else {
            this.append(entry);
        }
        this.kv.put(key, entry);
    }

    private void append(Node v) {
        v.prev = this.tail;
        v.prev.next = v;
        v.next = null;
        this.tail = v;
    }

    private void remove(Node v) {
        if (v.prev != null) {
            v.prev.next = v.next;
        }

        if (v.next != null) {
            v.next.prev = v.prev;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
