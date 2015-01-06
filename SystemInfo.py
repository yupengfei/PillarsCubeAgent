import os

import psutil



def SystemDetail():
	sysInfoDict = {}
	
	osUname = GetUname()
	sysInfoDict['sysname'] = osUname[0]
	sysInfoDict['nodename'] = osUname[1]
	sysInfoDict['release'] = osUname[2]
	sysInfoDict['machine'] = osUname[3]

	cpuCount = GetCPUCount()
	sysInfoDict['cpucount'] = cpuCount

	cpuPercent = GetCPUPercent()
	sysInfoDict['cpupercent'] = cpuPercent[0]

	virtualMemory = GetVirtualMemory()
	sysInfoDict['totalvirtualmemory'] = virtualMemory[0]
	sysInfoDict['availablevirtualmemory'] = virtualMemory[1]
	sysInfoDict['percentvirtualmemory'] = virtualMemory[2]
	sysInfoDict['usedvirtualmemory'] = virtualMemory[3]
	sysInfoDict['freevirtualmemory'] = virtualMemory[4]

	swapMemory = GetSwapMemory()
	sysInfoDict['totalswapmemory'] = swapMemory[0]
	sysInfoDict['usedswapmemory'] = swapMemory[1]
	sysInfoDict['freeswapmemory'] = swapMemory[2]
	sysInfoDict['percentmemory'] = swapMemory[3]

	diskUsage = GetDiskUsage()
	sysInfoDict['totaldisk'] = diskUsage[0]
	sysInfoDict['useddisk'] = diskUsage[1]
	sysInfoDict['freedisk'] = diskUsage[2]
	sysInfoDict['percentdisk'] = diskUsage[3]

	return sysInfoDict

def GetUname():
	return os.uname()

def GetCPUCount():
	return psutil.cpu_count()

def GetCPUPercent():
	return psutil.cpu_percent(interval=1, percpu=True)

def GetVirtualMemory():
	return psutil.virtual_memory()

def GetSwapMemory():
	return psutil.swap_memory()

def GetPartitions():
	return psutil.disk_partitions()

def GetDiskUsage():
	return psutil.disk_usage('/')

if __name__ == '__main__':
	sysInfoDict = SystemDetail()
	print(sysInfoDict)
	# cpuCount = GetCPUCount()
	# print(cpuCount)
	# cpuPercentList = GetCPUPercent()
	# print(cpuPercentList)
	# virtualMemory = GetVirtualMemory()
	# print(virtualMemory)
	# print(virtualMemory[2])
	# swapMemory = GetSwapMemory()
	# print(swapMemory)

	# partitions = GetPartitions()
	# print(partitions)
	# diskUsage = GetDiskUsage()
	# print(diskUsage)
