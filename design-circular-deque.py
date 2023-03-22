from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.que = deque()
        self.maxSize = k
        self.currSize = 0
        self.front = 0
        self.rare = 0

    def insertFront(self, value: int) -> bool:
        if self.currSize == self.maxSize:
            return False
        self.que.appendleft(value)
        self.currSize += 1
        self.rare += 1
        if self.rare == self.maxSize-1:
            self.rare = 0
        return True

    def insertLast(self, value: int) -> bool:
        if self.currSize == self.maxSize:
            return False
        self.que.append(value)
        self.currSize += 1
        self.rare += 1
        if self.rare == self.maxSize-1:
            self.rare = 0
        return True

    def deleteFront(self) -> bool:
        if self.currSize == 0:
            return False
        self.que.popleft()
        self.front += 1
        self.currSize -= 1
        return True

    def deleteLast(self) -> bool:
        if self.currSize == 0:
            return False
        self.que.pop()
        self.rare -= 1
        self.currSize -= 1
        return True

    def getFront(self) -> int:
        if self.currSize == 0:
            return -1
        return self.que[0]

    def getRear(self) -> int:
        if self.currSize == 0:
            return -1
        return self.que[-1]

    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
        return self.currSize == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()