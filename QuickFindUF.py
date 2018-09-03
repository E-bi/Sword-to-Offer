#动态连通性问题
class QuickFindUF1(object):
    bucket = []
    def initBucket(self, num):
        #初始化一个目标容器
        for i in range(num):
            self.bucket.append(i)
    def isConnected(self, p, q):
        #p,q是否相连
        return self.bucket[p] == self.bucket[q]

    #将p,q连接
    #扫描整个目标容器的办法
    def union(self, p, q):
        #将p,q连接
        #扫描整个目标容器的办法
        pid = self.bucket[p]
        qid = self.bucket[q]
        for i in range(len(self.bucket)):
            if self.bucket[i] == pid: #找到与第一个参数具有相同数值的id，
            #让其值等于第二个参数的值
                self.bucket[i] = qid
        return self.bucket


#动态连通性问题
#利用树的方法 (依旧不是太快)
class QuickFindUF2(object):
    bucket = []
    def initBucket(self, num):
        #初始化一个目标容器
        for i in range(num):
            self.bucket.append(i)
    def isConnected(self, p, q):
        #p,q是否相连
        return self.root(p) == self.root(q)

    #找元素的根节点
    def root(self, i):
        while i != self.bucket[i]:
            i = self.bucket[i]
        return i

    #将p,q连接
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.bucket[i] = j 

un = QuickFindUF2()
ins = un.initBucket(1000)
print(un.isConnected(2,5))
un.union(3,967)
print(un.isConnected(3,967))



