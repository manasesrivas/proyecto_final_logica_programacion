import colorama
import os
import sys
import pyfiglet
import msvcrt
import random
from main import *
RTS = colorama.Fore.RESET
R = colorama.Fore.LIGHTRED_EX
B = colorama.Fore.BLUE


DIGITS = '1234567890'



# genera el codigo del ticket
def generate_code() -> str:
    return "".join(random.sample(DIGITS, 4))

# genera un ticket nuevo
def generate_new_ticket() -> str:
    code = f'{generate_code()}-{generate_code()}-{generate_code()}'
    return code

def save_new_ticket(full_name: str, destination_to: str, passenger_type: str, ticket_cod, price: int):
    ticket = f'{ticket_cod},{full_name},{destination_to},{passenger_type},{price}\n'
    with open("./tickets.txt", "a") as file: 
        file.write(ticket)


keys_arrow = {
        b"H": lambda x: x-1,
        b"P": lambda x:  x+1
    }

keys_pressed = {
        b"\xe0": lambda x, y: keys_arrow[x](y),
}

def show_message(color,msg) -> None:
    print(f'{color}{pyfiglet.figlet_format(msg, font="doom", width=200)}')
    


def listen_key(menu_list, row, **kwargs):
    key_pressed = msvcrt.getch()
    if key_pressed == b"\r": menu_list[row-1]["func"](**kwargs)
    # if key_pressed == b"q": 

    second_code = msvcrt.getch() 
    if key_pressed in keys_pressed and second_code in keys_arrow:
        row = keys_pressed[key_pressed](second_code, row)

    return min(len(menu_list), max(1, row)) 

def init_menu(menu_list: list, menu_title):

    row = 1
    os.system("cls")
    
    show_message(colorama.Fore.YELLOW, menu_title)
    
    while True:
                

        sys.stdout.write(f'\033[{11};{0}H')
        for n, item in enumerate(menu_list):
            print(f'\r[{n+1}] {item["header"]}     ')
            
        sys.stdout.write(f'\033[{10+row};{0}H')
        print(f"{colorama.Fore.GREEN}{colorama.Back.LIGHTBLACK_EX} > [{row}] {menu_list[row-1]["header"]} <")

        row = listen_key(menu_list, row)

