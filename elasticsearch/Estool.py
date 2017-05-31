#coding=utf-8

from elasticsearch import Elasticsearch
import urllib2

class Nosql:

    def __init__(self,ip,port):
        self.host = ip
        self.port = port
        self.es = Elasticsearch([{'host':ip,'port':port}])

    def initDb(self,dbname):
        self.es.indices.create(dbname,ignore=[400])

    def selectDb(self,dbname,tableName):
        self.dbname = dbname
        self.tableName = tableName

    def setKv(self,k,v):
        self.es.index(index=self.dbname,doc_type=self.tableName,id=k,body=v)

    def getKv(self,k):
        return self.es.get(index=self.dbname,doc_type=self.tableName,id=k,ignore=[404])

    def remove(self,k):
        return self.es.delete(index=self.dbname,doc_type=self.tableName,id=k)

    # 'hits']['count 是查找的数目
    # 排序方式，只支持増序排列,不支持降序
    def qfind(self,q,sort=None,offset=0,size=3):
        return self.es.search(index=self.dbname,doc_type=self.tableName,q=q,from_=offset,sort=sort,size=size)

    # 降序查找数据
    def rfind(self,q,sort=None,offset=9,size=3):
        _c = self.es.count(index=self.dbname,doc_type=self.tableName,q=q)['count']
        _offset = _c - size
        if _offset <= 0 :
            _offset = 0
        return self.es.search(index=self.dbname,doc_type=self.tableName,q=q,from_=_offset,size=size,sort=sort)

    ## you need delete_by_query plugins
    # http://x.x.x.x:9200/_cat/plugins to see if has delete_by_query plugin
    # ./plugin install delete-by-query 安装插件
    # Elasticsearchpy does not have delete_by_query method 
    # So I write one by urllib, but it can only pass an query string
    def rremove(self,q):
        url = "http://%s:%d/%s/%s/_query?q=%s" % (self.host,self.port,self.dbname,self.tableName,q)
        _request = urllib2.Request(url)
        _request.get_method = lambda:'DELETE' 
        return urllib2.urlopen(_request).read()

if __name__ == "__main__":
    import datetime
    import json
    import pdb
    n = Nosql('10.210.12.18',9200)
    n.initDb("byworld")
    n.selectDb("byworld","sample")

    #for i in range(100,200):
    #    n.setKv('Sample_sort_' + str(i) ,{'check':0,'sort':i})

    #o = n.getKv("A_2")

    items = n.qfind('check:0','sort')
    print items['hits']['total']
    if items['hits']['total'] > 0 :
        for item in items['hits']['hits']:
            print item['_source']['sort']

    print "# " * 10
    items = n.rfind('check:0','sort')
    print items['hits']['total']
    if items['hits']['total'] > 0 :
        for item in items['hits']['hits']:
            print item['_source']['sort']

    print n.rremove('content:B')

