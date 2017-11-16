import socket
import os

s = socket.socket()
s.connect(("localhost",3988))
# Run command to check system specs and store in output.txt
os.system('top -n 1 -b | head -n 10 > output.txt')

f = open('output.txt','r')
f1 = open('response.txt','w+')
data = f.read() # can specify how much data of output is needed to be sent

s.send(data)
print("Reached here")
d = s.recv(1000)
print(d)

s.close()
