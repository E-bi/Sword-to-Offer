class TwoStackQueue:
    stackPush = []
    stackPop = []
    def appendTail(self,num):
        self.stackPush.append(num)

    def deleteHead(self):
        while self.stackPush:
            data = self.stackPush.pop()
            self.stackPop.append(data)
        if self.stackPop is None:
            raise Exception("queue is empty")
        head = self.stackPop.pop()
        return head
Queue = TwoStackQueue()
Queue.appendTail(7)
print(Queue.deleteHead())
