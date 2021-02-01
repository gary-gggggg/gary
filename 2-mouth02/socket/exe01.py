import socket
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.bind(("0.0.0.0",31415))

