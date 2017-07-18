#coding=utf-8

import kubernetes
import base64

h = ""
kubernetes.client.Configuration().host = h
kubernetes.client.Configuration().api_key = { "authorization" : "Basic %s" % (base64.b64encode("admin:admin")) }

api_instance = kubernetes.client.CoreV1Api()

# find node 
# nodes = api_instance.list_node().items
# 
# for node in nodes:
# 	print ""
# 	print node.metadata.name , node.metadata.labels
# 

pods = api_instance.list_pod_for_all_namespaces().items

for pod in pods:
	is_busy_box = False
	mt = pod.metadata
	containers = pod.spec.containers
	for c in containers :
		is_busy_box = c.image.find("busybox") != -1 

	if is_busy_box :
		print "name:%s , labels:%s , ns: %s , image: %s \n" % (mt.name,mt.labels,mt.namespace,c.image)
 
#  name = "pwn"
#  ns = "default"
#  body = swagger_client.V1DeleteOptions()
#  try:
#  	api_instance.delete_namespaced_pod(name,ns,body)
#  	print "DEL OK !"
#  except  Exception,e:
#  	print e 

