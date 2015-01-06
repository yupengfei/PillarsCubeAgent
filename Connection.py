import urllib.request
import urllib.parse
import time
import random

import SystemInfo

IPAdress = 'localhost'
Port = 5678
Interval = 100

def RandomMagicString():
	magicNumber = random.randint(0, 10000000000)
	return str(magicNumber)
def Heart():
	magicNumber = RandomMagicString()
	while True:
		sysInfoDict = SystemInfo.SystemDetail()
		params = urllib.parse.urlencode(sysInfoDict)
		url = 'http://' + IPAdress + ':' + str(Port) + "/heart?%s" %params + "&magicnumber=" + magicNumber
		#print(url)
		f = urllib.request.urlopen(url)
		#print(f.read().decode('utf-8'))
		time.sleep(Interval)


if __name__ == '__main__':
	Heart()
	# for i in range(10):
	# 	print(RandomMagicString())

