import http.server
import os

class MyHttpHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		if '/exe' in self.path:
			command, parametersDict = QuerySplit.SplitQuery(self.path)
			clientAddress = self.client_address[0] + str(self.client_address[1])
			print('clientAddress: ' + clientAddress)
			if command == 'command':
				print('heart')
				SendMessage(self, 'true')
				result = RunExe(parametersDict['shell'])

def SendMessage(requestInstance, message):
	r_str=message  
	enc="UTF-8"
	encoded = r_str.encode(enc)  
	requestInstance.send_response(200)  
	requestInstance.send_header("Content-type", "text/html; charset=%s" % enc)  
	requestInstance.send_header("Content-Length", str(len(encoded)))  
	requestInstance.end_headers()
	requestInstance.wfile.write(encoded)

def RunExe(commandString):
	result = os.system(commandString)
	return result

if __name__ == '__main__':
	result = RunExe('ls')
	print(result)