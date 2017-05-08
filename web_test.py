# -*- coding: utf-8 -*-

import threading, time
import os , sys ,httplib

class config :
    increse_delay   = 5
    increse_thread  = 5
    increse_times   = 5
    thread_count    = 5
    #线程数达到最大值的时间
    process_time    = 10
    result          = False
    url             = 'https://www.baidu.com/s?ie=UTF-8&wd=httplib'
    method          = 'get' # 'post'
    headers         = {'Content-type': 'application/x-www-form-urlencoded'}
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

    def parseUrl(self,url):

        _url_a = url.split("://")
        _url_aa = _url_a[1].split("/")
        _url_aae = "/".join(_url_aa[1:])

        if _url_aae == "" :
            _url_aae = "/"
        else :
            _url_aae = "/" + _url_aae

        return (_url_a[0],_url_aa[0],_url_aae)


    def runSingleRequest(self):
        global config

        _post_data = config.post_data

        (scheme,host,others) = self.parseUrl(config.url)

        if scheme == "http" :
            _con = httplib.HTTPConnection(host)
        else :
            _con = httplib.HTTPSConnection(host,443,config.key_file,config.cert_file,True,10)

        if config.method == "get" :
            _con.request("GET",others,'',config.headers)
        else :
            _con.request("POST",others,config.post_data,config.headers)

        response = _con.getresponse()
        if response.status == 200:
            config.result.setOk()
        else :
            config.result.setFailed()
                 
        _con.close()


    def run(self):
        while True:
            self.runSingleRequest()

def showTimeDetail(delay,count,c = "#"):
    for _ in range(count):
        time.sleep(delay)
        print c,
    print 

def runWebTest():

    global config 

    config.result = Result()
    threads = []

    for i in range(0,config.thread_count):
        t = RequestThread(i)
        threads.append(t)
        t.start()

    print "%d threads requesting ..." % (len(threads))

    for ik in range(0,config.increse_times):
        delay = config.increse_delay
        showTimeDetail(0.5,delay * 2)
        for ic in range(0,config.increse_thread) :
            t = RequestThread(i + ic)
            threads.append(t)
            t.start()
        print "%d threads requesting ..." % (len(threads))

    print "Keep alive for %d seconds , you are great !" % (config.process_time)
    showTimeDetail(0.5,config.process_time * 2)
    config.result.report()

def debugRequest():
    config.result = Result()
    RequestThread(0).start()
    time.sleep(1)
    config.result.report()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    #runWebTest()
    debugRequest()
