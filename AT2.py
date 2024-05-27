import csv
import platform
import uuid 
import socket
import speedtest
import datetime

# Dictionary 
info = {} 

# Computer name
info["Computer Name"] = socket.gethostname()

# IP address
info["IP Address"] = socket.gethostbyname(socket.gethostname())

# MAC address
info["MAC Address"] = hex(uuid.getnode())

# Processor name 
processorName = platform.processor() 

# Adding processor name to dictionary. 
info["Processor Model"] = processorName 

# Platform details 
platformDetails = platform.platform() 

# Adding platform details to dictionary. 
info["Operation System"] = platformDetails 

# ct stores current time.
ct = datetime.datetime.now()
info["System Time"] =  ct

def perform_speed_test():
   st = speedtest.Speedtest()
   downloadSpeed = st.download() / 1000000  # Convert to Mbps
   return round(downloadSpeed, 2)

downloadSpeed = perform_speed_test()
info["Internet Connection Speed"] = str(downloadSpeed) + " Mbps"


# Simple port scanning
ip = socket.gethostbyname (socket.gethostname()) # Getting ip-address of host

ports = ""

for port in range(65535):	 # Check for all available ports

	try:
		serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Create a new socket
		serv.bind((ip,port)) # Bind socket with address
			
	except:
		if ports == "":
			ports = str(port)
		else:
			ports = ports + ";" + str(port)
		
	serv.close() # Close connection

# Adding active ports to dictionary.
info["Active Ports"] =  ports

# Printing the dictionary details 
for i, j in info.items(): 
	print(i, " - ", j) 
	
file = "computers.csv"

# Reading csv file and checking the MAC address.
with open(file, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    macExists = False
    for row in reader:
        macAddress = row["MAC Address"]
        print(macAddress + " has been read")
		# MAC address is already in file
        if macAddress == info["MAC Address"]:
            print("computer already added to file")
            macExists = True

csvfile.close()

# Writing information to csv file if MAC address does not exist.
if macExists == False:
    try:
        csvfile = open(file, "a")
        writer = csv.DictWriter(csvfile, fieldnames=list(info.keys()))
        writer.writerow(info)
        csvfile.close()
        print("computer added to csv file")
    except:
        print("error writing to csv file")