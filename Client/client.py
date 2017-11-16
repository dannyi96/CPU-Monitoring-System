import socket
import os


s = socket.socket()
s.connect(("localhost",3948))
# Run command to check system specs and store in output.txt
os.system('top -n 1 -b | head -n 10 > Sent\ Files/output.txt')

f = open('Sent Files/'+'output.txt','r')
recv = open('Received Files/'+'recv.txt','w+')
data = f.read() # can specify how much data of output is needed to be sent

s.send(data)
print("Reached here")
d = s.recv(1024)
print(d)
recv.write(d)

s.close()
