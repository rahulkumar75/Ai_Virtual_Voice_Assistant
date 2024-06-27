print("hello")
from colorama import init, Fore, Back, Style    # pip install colorama

# Initialize colorama
init()


print(Fore.RED + "This text is red!")
print(Back.GREEN + "This text has a green background!")
print(Style.BRIGHT + "This text is bright!")
print(Style.RESET_ALL)  # Reset all styles
print(Style.RESET_ALL + Fore.YELLOW + Style.NORMAL + "This text is bright!")