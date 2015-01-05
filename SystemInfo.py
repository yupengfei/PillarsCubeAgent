import os

import psutil

sysInfoDict = {}

def SystemDetail():
	
def GetUname():
	
	sysInfo = os.uname()
	sysInfoDict['sysname'] = sysInfo[0]
	sysInfoDict['nodename'] = sysInfo[1]
	sysInfoDict['release'] = sysInfo[2]
	sysInfoDict['machine'] = sysInfo[3]

	

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
	sysInfoDict = GetUname()
	print(sysInfoDict)
	cpuCount = GetCPUCount()
	print(cpuCount)
	cpuPercentList = GetCPUPercent()
	print(cpuPercentList)
	virtualMemory = GetVirtualMemory()
	print(virtualMemory)
	print(virtualMemory[2])
	swapMemory = GetSwapMemory()
	print(swapMemory)

	partitions = GetPartitions()
	print(partitions)
	diskUsage = GetDiskUsage()
	print(diskUsage)
