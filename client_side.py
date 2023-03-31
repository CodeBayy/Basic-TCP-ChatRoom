import socket
import threading
import sys

print('Welcome Soldier..')
print("-----------------")

nickname = input("Choose your nickname: ")
ip_addr = input('Enter IpAddress: ')
port_num = int(input('Enter PortNum: '))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_addr,port_num))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'exit':
                break
            else:
                print(message)
        except:
            print("No Error Occured")
            client.close()
            break 
        
def write():
    while True:
        message = f" {nickname}: {input('')}"
        # message = input(f"{nickname}: ")
        client.send(message.encode('ascii'))
        if message == 'exit':
            break
        else:
            continue
        

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
