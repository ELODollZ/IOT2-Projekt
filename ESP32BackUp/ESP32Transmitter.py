import socket

HOST = "192.168.239.54" #The RPI
PORT = 1883 #The Port of the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello wOrld")
    data = s.recv(1024)

print(f"Received {data!r}")