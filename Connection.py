import urllib.request
import urllib.parse

import SystemInfo

IPAdress = 'localhost'
Port = 5678

def Heart():
	sysInfoDict = SystemInfo.GetUname()
	params = urllib.parse.urlencode(sysInfoDict)
	url = 'http://' + IPAdress + ':' + str(Port) + "/heart?%s" %params
	print(url)
	f = urllib.request.urlopen(url)
	print(f.read().decode('utf-8'))

if __name__ == '__main__':
	Heart()

