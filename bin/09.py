class TwoStackQueue:
    stackPush = []
    stackPop = []
    def appendTail(self,num):
        self.stackPush.append(num)

    def deleteHead(self):
        while self.stackPush:
            self.stackPop.append(self.stackPush.pop())
        if not self.stackPop:
            raise Exception("queue is empty")
        return self.stackPop.pop()
Queue = TwoStackQueue()
Queue.appendTail(7)
print(Queue.deleteHead())

