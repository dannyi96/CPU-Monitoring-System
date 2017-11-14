import socket

def parseData(dataFile):
	l = []
	for line in dataFile:
		l.append(line.split())
	l = l[1:]
	l[0] = ["Tasks",l[0][1],l[0][3],l[0][5],l[0][7],l[0][9]]
	l[1] = ["CPU", l[1][1],l[1][3],l[1][5],l[1][7],l[1][9]]
	l[2] = ["Memory",l[2][3],l[2][5],l[2][7]]
	del l[3]
	del l[3]
	del l[3]
	l[3] = ["Process 1",l[3][0],l[3][1],l[3][8],l[3][9]]
	l[4] = ["Process 2",l[4][0],l[4][1],l[4][8],l[4][9]]
	del l[5]
	print(l)
	analyze(l)

s = socket.socket()
s.bind(("localhost",3030))
s.listen(10)
i = 0
j = 0
def analyze(l):
	for elem in l:
		if(elem[0] == "Tasks"):
			if(int(elem[1])>250):
				toSendFile.write("Too many Total Tasks\n")
			else:
				toSendFile.write("Total Number of Tasks is normal\n")
			if(int(elem[2])>10):
				toSendFile.write("Too many running tasks\n")
			else:
				toSendFile.write("Number of running tasks is normal\n")
		if(elem[0]=="CPU"):
			if(float(elem[1])>1.0):
				toSendFile.write("Too many user processes\n")
			else:
				toSendFile.write("Number of user processes is normal\n")
			
			if(float(elem[2])>0.5):
				toSendFile.write("Too many system processes\n")
			else:
				toSendFile.write("Number of system processes is normal\n")
		if(elem[0]=="Memory"):
			if(int(elem[1])-int(elem[3])<150000):
				toSendFile.write("Too much Memory usage\n")
			else:
				toSendFile.write("Normal Memory usage\n")
		 
	toSendFile.write("Current Processes\n")
	toSendFile.write("Process \t\t CPU % \t \t Memory usage")
	toSendFile.write("%s \t \t %s \t \t %s" %(l[3][2],l[3][3],l[3][4]))
	toSendFile.write("%s \t \t %s \t \t %s" %(l[4][2],l[4][3],l[4][4]))
	toSendFile.seek(0,0)

while(True):
	sc,address = s.accept()
	print(address)
	print("port number is : ",int(address[1]))
	f = open('file_' + str(i) + '.txt','w+')
	toSendFile = open('send_'+str(j)+'.txt','w+')
	i += 1
	j += 1
	l = sc.recv(1024)
	while(l):
		f.write(l)
		l = sc.recv(1024)
	f.seek(0,0)
	parseData(f)
	data = toSendFile.read()
	# CHeck how to send
	#s.send(data)
	f.close()
	sc.close()

s.close()	

