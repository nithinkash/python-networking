import socket

#setting up the host and port 
target_host="0.0.0.0"
target_port=2560	#http deafault port

#socket object with ipv4 and tcp 
client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to host 
client.connect((target_host,target_port))

#send some data
client.send(("GET / HTTP/1.1\r\nHost: www.google.com\n\r\n\r"))

#getting back response
response = client.recv(4096)

print(response)
