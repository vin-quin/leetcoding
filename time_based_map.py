# https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap:

    def __init__(self):
        self.kv = {} # key: [values]
        self.timestamps = {} # key: [timestamps]

    def set(self, key: str, value: str, timestamp: int) -> None: 
        # timestamps only ever increase so we can always append
        v = self.kv.get(key, [])
        v.append(value)
        self.kv[key] = v

        v = self.timestamps.get(key, [])
        v.append(timestamp)
        self.timestamps[key] = v

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        
        idx = search(self.timestamps[key], timestamp, 0, len(self.timestamps[key])-1)
        return self.kv[key][idx] if idx >= 0 else "" # Return last value is we dont find one for this key

# high low
# 10   20
def search(arr: list[int], timestamp: int, l: int, r: int) -> int:
    if r < l:
        return l-1

    mid = l+(r-l)//2
    if arr[mid] == timestamp:
        return mid
    
    if timestamp < arr[mid]:
        return search(arr, timestamp, l, mid-1)
    else:
        return search(arr, timestamp, mid+1, r)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


def main():
    timeMap = TimeMap()
    (timeMap.set("foo", "bar", 1))  # store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 0))         # return "bar"
    print(timeMap.get("foo", 1))         # return "bar"
    print(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    (timeMap.set("foo", "bar2", 4)) # store the key "foo" and value "bar2" along with timestamp = 4.
    print(timeMap.get("foo", 4))         # return "bar2"
    print(timeMap.get("foo", 5))         # return "bar2"

if __name__ == '__main__':
    main()