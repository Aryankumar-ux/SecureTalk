import os
import time
import sys
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, color=Fore.CYAN, delay=0.1):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def header():
    clear_screen()
    print()
    animate_text(">>>  PIN CODE ENCRYPTOR TOOL  <<<", Fore.MAGENTA, 0.1)
    print(Fore.YELLOW + Style.BRIGHT + "\nDeveloped by Aryan Kumar")
    print(Fore.YELLOW + "WhatsApp: +91 9931905995")
    print(Fore.LIGHTBLACK_EX + "-" * 40)
    print()

def main_menu():
    print(Fore.GREEN + '1. Normal Mode')
    print(Fore.CYAN + '2. Secure Mode (Password Protected)')
    print(Fore.YELLOW + '3. About This Tool')
    print(Fore.RED + '4. Quit')
    print(Fore.LIGHTWHITE_EX + '\nPress Ctrl + Z to stop\n')

def normal_mode():
    print(Fore.CYAN + "1. Encode")
    print(Fore.GREEN + "2. Decode")
    inp1 = input(Fore.LIGHTBLUE_EX + 'Enter your choice: ')
    if inp1 == '1':
        while True:
            os.system('python encode2.py')
    elif inp1 == '2':
        os.system('python decode2.py')
    else:
        print(Fore.RED + 'Wrong input')

def secure_mode():
    print(Fore.CYAN + "1. Encode")
    print(Fore.GREEN + "2. Decode")
    inp2 = input(Fore.LIGHTBLUE_EX + 'Enter your choice: ')
    if inp2 == '1':
        while True:
            os.system('python Encode.py')
    elif inp2 == '2':
        while True:
            os.system('python Decode.py')
    else:
        print(Fore.RED + 'Wrong input')

def about():
    clear_screen()
    print(Fore.YELLOW + Style.BRIGHT + "This tool allows secure chatting using encryption.")
    print(Fore.YELLOW + "Developer: Aryan Kumar")
    print(Fore.YELLOW + "WhatsApp: +91 9931905995")
    time.sleep(10)
    os.system('python Start.py')

# Run program
header()
main_menu()

inp = input(Fore.LIGHTWHITE_EX + 'Enter your choice: ')
if inp == '1':
    normal_mode()
elif inp == '2':
    secure_mode()
elif inp == '3':
    about()
elif inp == '4':
    print(Fore.GREEN + 'Thanks for using it!')
    sys.exit()
else:
    print(Fore.RED + 'Wrong input')
    time.sleep(0.5)
    os.system('python Start.py')
