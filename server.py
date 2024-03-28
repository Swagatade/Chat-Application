import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 50847))
server.listen()  # Set the backlog to 1

print("Server listening on port...")

client, addr = server.accept()
print(f"Connection established with {addr}")

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print("Received:", msg)
    
    reply = input("Enter message to send: ")
    client.send(reply.encode('utf-8'))

print("Closing connection...")
client.close()
server.close()
