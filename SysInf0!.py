# By Crypt0o -- Copyright

import os
import platform
import psutil

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """
    

  _________            .___        ____________ ._.
 /   _____/__.__. _____|   | _____/ ____\   _  \| |
 \_____  <   |  |/  ___/   |/    \   __\/  /_\  \ |
 /        \___  |\___ \|   |   |  \  |  \  \_/   \|
/_______  / ____/____  >___|___|  /__|   \_____  /_
        \/\/         \/         \/             \/\/




    By Crypt0o -- Copyright   
    """
    print(banner)

clear_screen()
display_banner()

def system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    system_info()
