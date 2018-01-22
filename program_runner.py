import socket_connector_client
import socketconnector

def which():
    global answer
    try:
        answer = int(input('Would you like to:\n'
                       '\t 1.) Host this program? \n'
                       '\t 2.) Connect to a client? \n'
                       'Answer: '))
        if answer == 1:
            print(answer)
        elif answer == 2:
            print(answer)
        else:
            print("Please enter in either '1' or '2'")
            which()
    except:
        print('Please enter in some valid input you here.')
        which()
    return answer

which()





if answer == 1:
    print('Congrats, you are now hosting this file.')
    socketconnector.Main()
elif answer == 2:
    print('Congrats, you are now the client for this thing.')
    socket_connector_client.Main()



