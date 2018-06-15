import queue
import threading
class Job(object):
    def __init__(self,priority,des):
        self.priority = priority
        self.des = des
        print('New Job:',des)
        return    
    def confine(priority,des):
        return (self.priority,self,des)
q= queue.PriorityQueue()
print(Job(3,'ddddd'))
#q.put((3,Job('优先级为3')))  #put的参数需要为元组
#q.put((1,Job('优先级为1')))
#q.put((8,Job('优先级为8')))

def process_job(q):
    while True:
        next_job = q.get()
        print('Job',next_job[1].des)
        q.task_done() #手动调用，告诉队列当前任务已经完成
workers = [
            threading.Thread(target=process_job,args=(q,)),
            threading.Thread(target=process_job,args=(q,))
            ]
for work in workers:
    work.setDaemon(True)
    work.start()
q.join()
