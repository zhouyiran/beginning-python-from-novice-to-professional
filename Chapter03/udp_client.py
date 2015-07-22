__author__ = 'Administrator'

import socket, sys

host = '127.0.0.1'
textport = 8125

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')
s.connect((host, port))
while 1:
    print "Enter data to transmit:"
    data = sys.stdin.readline().strip()
    s.sendall(data)
    print "Looking for replies; press Ctrl-C or Ctrl-Break to stop."
    print "\n"


