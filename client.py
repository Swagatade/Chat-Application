import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 50847))

try:
    done = False

    while not done:
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        if response == "quit":
            done = True
        else:
            print("Server response:", response)

except Exception as e:
    print("Error:", e)

finally:
    client.close()
