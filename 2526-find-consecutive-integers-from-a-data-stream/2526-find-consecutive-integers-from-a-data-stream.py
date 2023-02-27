class DataStream:

    def __init__(self, value: int, k: int):
        self.store = deque()
        self.value = value
        self.length = k
        self.count = 0
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.count = 0
            
        elif num == self.value:
            self.count += 1
            self.store.append(self.value)
            
        if self.count >= self.length:
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)