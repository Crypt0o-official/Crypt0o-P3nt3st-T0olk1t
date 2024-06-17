#By Crypt0o -- Copyright

import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = """
    

__________.__                  _______  ___________._.
\______   \__| ____    ____    \   _  \ \_   _____/| |
 |     ___/  |/    \  / ___\   /  /_\  \ |    __)  | |
 |    |   |  |   |  \/ /_/  >  \  \_/   \|     \    \|
 |____|   |__|___|  /\___  /____\_____  /\___  /    __
                  \//_____/_____/     \/     \/     \/



    By Crypt0o -- Copyright
    """
    print(banner)

clear_screen()
display_banner()

def ping_test(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

if __name__ == "__main__":
    host = input("Enter the IP address or domain to ping: ")
    ping_test(host)
