import urllib2 as brouser
print brouser.urlopen.__doc__

content=brouser.urlopen(¨http://class.aarmontech.com/1/bulb.txt¨)
print content.read()
