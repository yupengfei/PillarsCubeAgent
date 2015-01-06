import time
import _thread

import Connection

def timer(no, interval):
	print("timer")
	cnt = 0
	while cnt < 10:
		print('ThreadL(%d) Time:%s\n'%(no, time.time()))
		time.sleep(interval)
		cnt += 1
	_thread.exit_thread()

def test():
	_thread.start_new_thread(timer, (1, 1))
	_thread.start_new_thread(timer, (2, 2))
	return

def MultiThread():
	for i in range(1000):
		time.sleep(0.01)
		_thread.start_new_thread(Connection.Heart, ())

if __name__ == '__main__':
	print("thread")
	MultiThread()
	a = input("wating")