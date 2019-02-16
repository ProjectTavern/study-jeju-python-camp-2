from urllib2 import urlopen

data = "query=python"
f = urlopen("http://paullab.co.kr/", data)
print f.read(300)