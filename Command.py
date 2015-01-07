import os

def RunExe(commandString):
	result = os.system(commandString)
	return result

if __name__ == '__main__':
	print("running")
	result = RunExe('sudo shutdown -h now')
	print(result)