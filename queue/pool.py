from multiprocessing import Pool
import os,time

def f(x):
    print "This is " , x
    time.sleep(1)

pool = Pool(processes=3)    # set the processes max number 3
for i in range(11,20):
    ## params import ,
    result = pool.apply_async(f, (i,))

pool.close()
pool.join()

if result.successful():
    print result
    print 'successful'

