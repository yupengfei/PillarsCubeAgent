import os
import urllib.parse

def RunExe(commandString):
	result = os.system(urllib.parse.unquote(commandString))
	return result

if __name__ == '__main__':
	print("running")
	result = RunExe('ls%20/%20%3E%20/home/developer/test.txt')
	print("result" + str(result))