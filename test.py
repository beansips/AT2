import socket

ip = socket.gethostbyname (socket.gethostname()) #getting ip-address of host

ports = ""

for port in range(65535):	 #check for all available ports

	try:

		serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket

		serv.bind((ip,port)) # bind socket with address
			
	except:

		print('[OPEN] Port open :',port) #print open port number
		if ports == "":
			ports = str(port)
		else:
			ports = ports + ";" + str(port)
		print(ports)

	serv.close() #close connection