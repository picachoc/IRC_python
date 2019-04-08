import socket
import select
import datetime

'''if(len(sys.argv)==0):
    printf("Error : please specify the chat's IP adress.")'''

HOST = "127.0.0.1" #the parameter of the program call will be the chat's IP adress
PORT = 7777
nick = ""

# Encode the client 
def string_to_PICROM(string):
    if(string[0]=='/'):
        return (string)[1:].upper().encode() #we delete the '/' and turn the string into capital letters
    return ('MSG'+string).upper().encode()


def PICROM_to_string(data):
    data.decode()

    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    msg=input('nick : ')
    s.send(string_to_PIGROM(msg))
            

print('Received', repr(data))