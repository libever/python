#coding=utf-8

import xml.dom.minidom as xdom
import datetime

gpx_head = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<gpx version="1.1" creator="Movescount - http://www.movescount.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.cluetrust.com/XML/GPXDATA/1/0 http://www.cluetrust.com/Schemas/gpxdata10.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd" xmlns:gpxdata="http://www.cluetrust.com/XML/GPXDATA/1/0" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns="http://www.topografix.com/GPX/1/1">
<trk>
    <name>%s</name>
    <trkseg>
"""

gpx_end = """    </trkseg>
  </trk>
</gpx>"""


def parse_gpx_file(filename):
    content = open(filename,"r").read()
    dom = xdom.parseString(content)
    points = dom.getElementsByTagName("trkpt")
    results = []
    for point in points:
        lat = point.getAttribute("lat")
        lon = point.getAttribute("lon")
        ele = point.getElementsByTagName("ele")[0].childNodes[0].data
        time = point.getElementsByTagName("time")[0].childNodes[0].data
        results.append({'lat':lat,'lon':lon,'ele':ele,'time':time})
    return results

def rewrite_pgx_file(filename,tofilename,start_time,seconds,new_gpx_name):
    global gpx_head
    global gpx_end
    t_time = start_time
    points = parse_gpx_file(filename)
    to_file = open(tofilename,"w")
    to_file.write(gpx_head % (new_gpx_name))
    for point in points:
       t_time = t_time + datetime.timedelta(seconds=seconds)
       t_str = t_time.isoformat() + "Z"
       n_point = """      <trkpt lat="%s" lon="%s">
        <ele>%s</ele>
        <time>%s</time>
      </trkpt>
""" % (point["lat"],point["lon"],point["ele"],t_str)
       to_file.write(n_point)
    to_file.write(gpx_end)
    to_file.close()

points = parse_gpx_file("./New_gpx.gpx")
start_time = datetime.datetime(2017, 4, 16)
seconds = 14
rewrite_pgx_file("./TNF100_Beijing_50km.gpx","./Test.gpx",start_time,14,"custome tnf 50")
exit(0)

new_gpx_file = open("New_gpx.gpx","w")
new_gpx_file.write(gpx_head)

f = datetime.datetime(2017, 4, 16)

#print f.isoformat()

#exit(0)
"""
解析gpx文件
"""
content = open("./TNF100_Beijing_50km.gpx","r").read()
dom = xdom.parseString(content)
points = dom.getElementsByTagName("trkpt")

index = 0 

for i in points:
    lat = i.getAttribute("lat")
    lon = i.getAttribute("lon")
    ele = i.getElementsByTagName("ele")[0].childNodes[0].data
    time = i.getElementsByTagName("time")[0].childNodes[0].data
    index = index + 1
    f =  f + datetime.timedelta(seconds=14)
    nt = f.isoformat() + "Z"
    #print index , lat,lon , ele,time

    n_point = """      <trkpt lat="%s" lon="%s">
        <ele>%s</ele>
        <time>%s</time>
      </trkpt>
""" % (lat,lon,ele,nt)
    new_gpx_file.write(n_point)
    print index , lat,lon , ele,nt

new_gpx_file.write(gpx_end)
new_gpx_file.close()
