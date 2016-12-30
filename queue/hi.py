import Queue
q = Queue.Queue(maxsize=10)

for i in range(0,10):
    q.put(i)


## if queue is full ,wait it's empty
## or block = 0 , 1 
## or timeout = 0 , 1
## cause an exception

try:
    q.put(3,timeout=1,block=0)
except Exception,e:
    print type(e)

for i in range(1,10):
    print q.get()
