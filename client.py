import socket
import os

s = socket.socket()
s.connect(("localhost",3000))

# Run command to check system specs and store in output.txt
os.system('top -n 1 -b > output.txt')

f = open('output.txt','r')

data = f.read() # can specify how much data of output is needed to be sent

s.send(data)

s.close()
