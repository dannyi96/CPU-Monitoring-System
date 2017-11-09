import socket

s = socket.socket()
s.bind(("localhost",3000))
s.listen(10)
i = 0

while(True):
	sc,address = s.accept()
	print(address)
	f = open('file_' + str(i) + '.txt','w')
	i += 1
	l = sc.recv(1024)
	while(l):
		f.write(l)
		l = sc.recv(1024)
	f.close()
	sc.close()

s.close()	

