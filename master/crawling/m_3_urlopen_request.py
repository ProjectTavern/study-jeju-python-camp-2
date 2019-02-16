from urllib2 import urlopen

req = urllib2.Request("http://paullab.co.kr")
req.add_header("Content-Type", "text/plain")
req.add_data("query=python")
f = urllib2.urloepn(req)
print f.read(300)