class MyCircularDeque:

    def __init__(self, k: int):
        self.que=[0]*k
        self.front=0
        self.end=-1
        self.counter=0
        self.k=k
    def insertFront(self, value: int) -> bool:
        if self.isFull()==True:
            return False
        else:
            self.front=(self.front-1)%self.k
            self.que[self.front]=value
            self.counter+=1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull()==True:
            return False
        else:
            self.end=(self.end+1)%self.k
            self.que[self.end]=value
            self.counter+=1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty()==True:
            return False
        else:
            self.front=(self.front+1)%self.k
            self.counter-=1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty()==True:
            return False
        else:
            self.end=(self.end-1)%self.k
            self.counter-=1
            return True
        
    def getFront(self) -> int:
        if self.counter==0:
            return -1
        return self.que[self.front]

    def getRear(self) -> int:
        if self.counter==0:
            return -1
        return self.que[self.end]

    def isEmpty(self) -> bool:
        if self.counter==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.counter==self.k:
            return True
        else:
            return False
            
        


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
