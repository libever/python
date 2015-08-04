#!/bin/sh

killall -9 uwsgi

echo "staring..."
sleep 2

cd /data1/simplepython/1

uwsgi -M -p 2 -t 30  -R 10000 -d /data1/uwsgilog/uwsgi.log --uid=www --gid=www --enable-threads -s /tmp/uwsgi.sock -w demo --check-static-docroot 

