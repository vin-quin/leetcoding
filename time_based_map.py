# https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap:

    def __init__(self):
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        

    def get(self, key: str, timestamp: int) -> str:
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


def main():
    TimeMap timeMap = TimeMap()
    print(timeMap.set("foo", "bar", 1))  # store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 1))         # return "bar"
    print(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    print(timeMap.set("foo", "bar2", 4)) # store the key "foo" and value "bar2" along with timestamp = 4.
    print(timeMap.get("foo", 4))         # return "bar2"
    print(timeMap.get("foo", 5))         # return "bar2"

if __name__ == '__main__':
    main()