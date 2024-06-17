# By Crypt0o -- Copyright

import os
import psutil
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """


 _______  ________  __          _______         __      _____  _______        ._.
 \      \ \_____  \/  |___  _  _\   _  \_______|  | __ /     \ \   _  \   ____| |
 /   |   \  _(__  <   __\ \/ \/ /  /_\  \_  __ \  |/ //  \ /  \/  /_\  \ /    \ |
/    |    \/       \  |  \     /\  \_/   \  | \/    </    Y    \  \_/   \   |  \|
\____|__  /______  /__|   \/\_/  \_____  /__|  |__|_ \____|__  /\_____  /___|  /_
        \/       \/                    \/           \/       \/       \/     \/\/




    By Crypt0o -- Copyright  
    """
    print(banner)

clear_screen()
display_banner()

def network_monitor(duration=10):
    print(f"Monitoring network activity for {duration} seconds...")
    net_io_start = psutil.net_io_counters()
    time.sleep(duration)
    net_io_end = psutil.net_io_counters()
    print(f"Bytes sent: {net_io_end.bytes_sent - net_io_start.bytes_sent}")
    print(f"Bytes received: {net_io_end.bytes_recv - net_io_start.bytes_recv}")

if __name__ == "__main__":
    duration = int(input("Enter the duration to monitor (seconds): "))
    network_monitor(duration)
