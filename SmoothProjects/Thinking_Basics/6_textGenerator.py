import pyfiglet
from colorama import Fore, init

# Initialize colorama for cross-platform color support
init()

name = input("Enter friend's name: ")

# Print formatted banner text in yellow
print(Fore.YELLOW + pyfiglet.figlet_format("Happy Birthday"))
print(Fore.YELLOW + pyfiglet.figlet_format(name))