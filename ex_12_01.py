import socket

url = input("Enter a URL: ")
host = url.split("/")


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host[2], 80))
except:
    print("Please enter a valid URL.")
    quit()
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()