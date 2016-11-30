def ApplicationInstance():    
    global pidfile    
    pidfile = open(os.path.realpath(__file__), "r")    
    try:    
        fcntl.flock(pidfile, fcntl.LOCK_EX | fcntl.LOCK_NB) #创建一个排他锁,并且所被锁住其他进程不会阻塞    
    except:    
        print "another instance is running..."    
        sys.exit(1)    
