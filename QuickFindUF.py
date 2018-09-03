#动态连通性问题
class QuickFindUF(object):
    bucket = []
    def initBucket(self, num):
        #初始化一个目标容器
        for i in range(num):
            self.bucket.append(i)
    def isConnected(self, p, q):
        #p,q是否相连
        return self.bucket[p] == self.bucket[q]
    def union(self, p, q):
        #将p,q连接
        pid = self.bucket[p]
        qid = self.bucket[q]
        for i in range(len(self.bucket)):
            if self.bucket[i] == pid: #找到与第一个参数具有相同数值的id，
            #让其值等于第二个参数的值
                self.bucket[i] = qid
        return self.bucket

un = QuickFindUF()
ins = un.initBucket(1000)
print(un.isConnected(2,5))
un.union(3,967)
print(un.isConnected(3,967))



