# By Crypt0o -- Copyright

import socket
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """
    

_________________          __  .________        _____       ._.
\______   \   _  \________/  |_|   ____/ ____  / ___ \  ____| |
 |     ___/  /_\  \_  __ \   __\____  \_/ ___\/ / ._\ \/    \ |
 |    |   \  \_/   \  | \/|  | /       \  \__<  \_____/   |  \|
 |____|    \_____  /__|   |__|/______  /\___  >_____\ |___|  /_
                 \/                  \/     \/             \/\/

        
    
    By Crypt0o -- Copyright
    """
    print(banner)

clear_screen()
display_banner()

def port_scanner(host):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

if __name__ == "__main__":
    host = input("Enter the IP address to scan: ")
    port_scanner(host)
