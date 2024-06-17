# By Crypt0o -- Copyright

import os
import socket
import psutil

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """


.____                   _____ .__ _________________          __   ____/\__
|    |    ____   ____  / ___ \|  |\______   \   _  \________/  |_/   / /_/
|    |   /  _ \_/ ___\/ / ._\ \  | |     ___/  /_\  \_  __ \   __\__/ / \ 
|    |__(  <_> )  \__<  \_____/  |_|    |   \  \_/   \  | \/|  | / / /   \
|_______ \____/ \___  >_____\ |____/____|    \_____  /__|   |__|/_/ /__  /
        \/          \/                             \/             \/   \/ 



    By Crypt0o -- Copyright   
    """
    print(banner)

clear_screen()
display_banner()

def local_ports():
    connections = psutil.net_connections()
    for conn in connections:
        if conn.status == 'LISTEN':
            print(f"Port {conn.laddr.port} is open (PID: {conn.pid})")

if __name__ == "__main__":
    local_ports()
