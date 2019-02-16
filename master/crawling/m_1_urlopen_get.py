from urllib2 import urlopen

f = urlopen("http://paullab.co.kr/")
print f.read(500)