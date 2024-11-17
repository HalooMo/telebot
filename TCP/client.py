import sys
import socket


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print(sys.argv)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sys.argv[1].encode("utf-8"))
    data = s.recv(1024)
    strdata = data.decode("utf-8")
    print(strdata)
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sys.argv[1].encode("utf-8"))
    data = s.recv(1024)
    strdata = data.decode("utf-8")
    print(strdata)
