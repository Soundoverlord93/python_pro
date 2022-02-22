import random
import pyfiglet
from termcolor import colored
import time
import sys
#Define custom exception class for main game logic exception
class UserNumError(Exception):
    pass

dict_msg = {"exit":"Goodbye !!!","wrng":"Wrong value entered, please enter  number between 0 and 10 ","more":"Your number is more than need, enter  number again : ","less":"Your number is less than need, enter  number again : ","win":"Congrats, you are guessed the number  !!!!","Hello":"Hello Player , enter your number between   0  and  10  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game"}

def msg(pnrt_val) :
    """function for printing  interacrive messages"""
    if pnrt_val == 'exit' :
        print(colored(pyfiglet.figlet_format(dict_msg["exit"]), "green"))
    elif(pnrt_val == 'wrng'):
        print(colored(dict_msg["wrng"],"red"), sep = "\n")
    elif(pnrt_val == 'more'):
        print(colored(dict_msg["more"], "red"))
    elif(pnrt_val == 'les'):
        print(colored(dict_msg["less"], "red"))
    elif(pnrt_val == 'win'):
        print(colored(pyfiglet.figlet_format(f'{dict_msg["win"]}',width = 180), "yellow"))
    else :
        print(colored(pyfiglet.figlet_format(dict_msg["Hello"], width = 190), "green"))


def usr_inp():
    """function for verifying user inputed data"""
    try:
        usr_inpt = input() # usr_inpt puted into try for KeyboardInterrupt catching
        if usr_inpt == 'exit':
            sys.exit(0)
        usr_inpt = int(usr_inpt)
    except ValueError:
        msg('wrng')
        return None
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        if 0 <= usr_inpt <=10 :
            return usr_inpt
        else:
            msg('wrng')
            return None
int_num = random.randint(0, 10) # Generate random number

def game_cnd(usernum):
    """ function for main game logic"""
    if usernum is None:
        raise UserNumError ('Wrng')
    elif usernum < int_num:
        msg('les')
    elif(usernum > int_num):
        msg('more')
    else:
        msg('win')
        time.sleep(5)
        sys.exit(0)

int_num = random.randint(0, 10) # Generate random number
msg(0)# Print Hello message
#print(int_num) # Print hint

#Main program cycle
while True:
    user_inpt = usr_inp()
    try:
        game_cnd(user_inpt)
    except UserNumError :
        continue


"""
Вроде все исправил только полностю функцию msg решил не заменять на словарь чтобы было удобно манипулировать выводом
"""


