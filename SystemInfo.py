import os

def GetUname():
	sysInfoDict = {}
	sysInfo = os.uname()
	sysInfoDict['sysname'] = sysInfo[0]
	sysInfoDict['nodename'] = sysInfo[1]
	sysInfoDict['release'] = sysInfo[2]
	sysInfoDict['machine'] = sysInfo[3]

	return sysInfoDict

if __name__ == '__main__':
	sysInfoDict = GetUname()
	print(sysInfoDict)