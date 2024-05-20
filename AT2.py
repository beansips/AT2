import csv
import platform
import uuid 
import socket
import speedtest
import datetime

# dictionary 
info = {} 

# computer name
info["Computer Name"] = socket.gethostname()

# ip address
info["IP Address"] = socket.gethostbyname(socket.gethostname())

# mac address
info["MAC Address"] = hex(uuid.getnode())

# processor name 
processor_name = platform.processor() 

# adding it to dictionary 
info["Processor Model"] = processor_name 

# platform details 
platform_details = platform.platform() 

# adding it to dictionary 
info["Operation System"] = platform_details 

# ct stores current time
ct = datetime.datetime.now()
info["System Time"] =  ct

def perform_speed_test():
   st = speedtest.Speedtest()
   download_speed = st.download() / 1000000  # Convert to Mbps
   return round(download_speed, 2)

download_speed = perform_speed_test()
info["Internet Connection Speed"] = str(download_speed) + " Mbps"


#Python code for simple port scanning
ip = socket.gethostbyname (socket.gethostname()) #getting ip-address of host

ports = ""

for port in range(65535):	 #check for all available ports

	try:
		serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
		serv.bind((ip,port)) # bind socket with address
			
	except:
		if ports == "":
			ports = str(port)
		else:
			ports = ports + ";" + str(port)
		
	serv.close() #close connection

info["Active Ports"] =  ports

# printing the details 
for i, j in info.items(): 
	print(i, " - ", j) 
	
file = "computers.csv"

with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    macExists = False
    for row in reader:
        mac_address = row['MAC Address']
        print(mac_address + " has been read")
		
        if mac_address == info["MAC Address"]:
            print("computer already added to file")
            macExists = True

csvfile.close()

if macExists == False:
    csvfile = open(file, 'a')
    writer = csv.DictWriter(csvfile, fieldnames=list(info.keys()))
    writer.writerow(info)
    csvfile.close()