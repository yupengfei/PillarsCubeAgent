import time
import _thread

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

if __name__ == '__main__':
	print("thread")
	test()
	a = input("wating")