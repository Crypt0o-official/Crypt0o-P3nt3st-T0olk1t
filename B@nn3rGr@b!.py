# By Crypt0o -- Copyright

import socket
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """
     

__________   _____               ________          ________         ________.  ._.
\______   \ / ___ \  ____   ____ \_____  \______  /  _____/______  / ___ \_ |__| |
 |    |  _// / ._\ \/    \ /    \  _(__  <_  __ \/   \  __\_  __ \/ / ._\ \ __ \ |
 |    |   <  \_____/   |  \   |  \/       \  | \/\    \_\  \  | \<  \_____/ \_\ \|
 |______  /\_____\ |___|  /___|  /______  /__|    \______  /__|   \_____\ |___  /_
        \/              \/     \/       \/               \/                   \/\/



    By Crypt0o -- Copyright                                         
    """
    print(banner)

clear_screen()
display_banner()

def banner_grab(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send(b'HEAD / HTTP/1.1\r\n\r\n')
        response = sock.recv(1024)
        print(response.decode('utf-8'))
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    host = input("Enter the IP address: ")
    port = int(input("Enter the port: "))
    banner_grab(host, port)
