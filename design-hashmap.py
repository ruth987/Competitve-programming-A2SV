class MyHashMap:

    def __init__(self):
        self.map = {}
        

    def put(self, key: int, value: int) -> None:
        # print(self.map)
        self.map[key] = value
        

    def get(self, key: int) -> int:
        # print(self.map)
        if key in self.map and self.map[key] != 10**7:
            return self.map[key]
        return -1
        

    def remove(self, key: int) -> None:
        # print(self.map)
        self.map[key] = 10**7

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)