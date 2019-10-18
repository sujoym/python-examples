import urllib2

url = 'http://pythonprogramming.net'
values = {'s':'basic' ,
          'submit':'search'}

data = urllib2.urlencode(values)
data = data.encode('utf-8')
req = urllib2.Request(url,data)
resp = urllib2.urlopen(req)
respData = resp.read()

print(respData)

