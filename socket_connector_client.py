import socket
import securechat
import logs

def host_ip():
    answer = input('Please enter in the IP address that you would like to connect to: ')
    trying_to_connect_to = answer
    logs.writer('Host is now trying to connect to: ' + trying_to_connect_to)
    return answer

def Main():
    host = host_ip()
    port = 5000
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host, port))
    while True:
        message = securechat.fixed(2)
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        recieved_message = securechat.decoding_el_message(str(data))
        logs.writer(recieved_message)
        print(recieved_message)

