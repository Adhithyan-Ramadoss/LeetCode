class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            self.values[self.keys.index(key)] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            return self.values[self.keys.index(key)]
        except ValueError:
            return -1

    def remove(self, key: int) -> None:
        try:
            _ = self.values.pop(self.keys.index(key))
            self.keys.remove(key)
        except ValueError:
            pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)