import random
import pyfiglet
from termcolor import colored
import time
import sys
#Define custom exception class for main game logic exception
class Win_exception(Exception):
    pass
class Wrng_exception(Exception):
    pass

#Define function for printing  interacrive messages
def msg(pnrt_val) :
    if pnrt_val == 'exit' :
        print(colored(pyfiglet.figlet_format("Goodbye !!!"), "green"))
    elif(pnrt_val == 'wrng'):
        print(colored("Wrong value entered, please enter  number between 0 and 10 ","red"), sep = "\n")
    elif(pnrt_val == 'more'):
        print(colored("Your number is more than need, enter  number again : ", "red"))
    elif(pnrt_val == 'les'):
        print(colored("Your number is less than need, enter  number again : ", "red"))
    elif(pnrt_val == 'win'):
        print(colored(pyfiglet.figlet_format(f"Congrats, you are guessed the number  !!!!",width = 180), "yellow"))
    else :
        print(colored(pyfiglet.figlet_format("Hello Player , enter your number between   0  and  10  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game", width = 190), "green"))

#Define function for verifying user inputed data 
def usr_inp():
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
#msg(0)# Print Hello message
print(int_num) # Print hint

#Define function for main game logic
def game_cnd(usernum):
    if usernum is None:
        raise Wrng_exception ('Wrng')
    elif usernum < int_num:
        msg('les')
    elif(usernum > int_num):
        msg('more')
    else:
        msg('win')
        raise Win_exception ('Win')

int_num = random.randint(0, 10) # Generate random number
msg(0)# Print Hello message
print(int_num) # Print hint

#Main program cycle
while True:
    user_inpt = usr_inp()
    try:
        game_cnd(user_inpt)
    except Wrng_exception :
        continue
    except Win_exception:
        time.sleep(5)
        break
        


"""
1)  Из usr_inp убрал цикл убралб также убрал искключения и передал None на выход функции

2) Упростил условие вхождения в диапазон

3) Но пришлось добавить два кастомних исключения в game_cnd() но можно и через функцию переделать...не знаю как лучше 

Рад замечаниям, буду исправлять 
"""


