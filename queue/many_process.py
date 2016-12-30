from multiprocessing import Process
import time

def fun(a,b,c):
    time.sleep(3)
    print a,b,c

p = Process(target=fun,args=(1,2,3))
p.start()
p.join()

print "OK GO"



