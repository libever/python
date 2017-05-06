# -*- coding: utf-8 -*-

import threading, time, httplib

class config :
    increse_seconds = 0
    increse_thread  = 0
    increse_times   = 0
    thread_count    = 5
    process_time    = 10
    result          = False
    url             = 'http://baidu.com'
    method          = 'get' # 'post'
    headers         = [] 
    post_data       = ""

class Result:

    def __init__(self):
        self.failedCount = 0
        self.okCount = 0
        self.reasons = []
        
    def setFailed(self,reason):
        self.failedCount = self.failedCount + 1
        self.reasons.append(reason)

    def setOk(self):
        self.okCount = self.okCount + 1

    def report(self):
        print "OK : %d "        % (self.okCount)
        print "Failed : %d "    % (self.failedCount)

class RequestThread(threading.Thread):

    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.daemon = True

    def run(self):
        global config
        while True:
            config.result.setFailed("")

def runWebTest():

    global config 
    config.result = Result()
    for i in range(0,config.thread_count):
        RequestThread(i).start()

    time.sleep(config.process_time)
    config.result.report()

if __name__ == "__main__":
    runWebTest()
