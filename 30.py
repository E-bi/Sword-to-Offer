import random
class StackWithMin():
    stack = []
    stack_min = []
    def pop(self):
        if not self.stack:
            raise Exception("stack is empty")
        pop_num = self.stack.pop()
        self.stack_min.remove(pop_num)
    def push(self,num):
        self.stack.append(num)
        if not self.stack_min: #如果为空则将其压入栈
            self.stack_min.append(num)
        if num < self.stack_min[-1]:
            self.stack_min.append(num)
        else:
            self.stack_min.append(self.stack_min[-1])
    def min(self):
        if self.stack_min == None or self.stack == None:
            raise Exception("stack is empty")
        pop_num = self.stack_min.pop()
        #self.stack.remove(pop_num)
        return pop_num

a = StackWithMin()
for i in range(15):
    num = random.randint(i,20)
    a.push(num)
print(a.stack)
print(a.min())
