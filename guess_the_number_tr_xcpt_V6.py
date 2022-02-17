import random
import pyfiglet
from termcolor import colored
import argparse
import time

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
        print(colored(f"Wrong value entered, please enter  number between {args['lower']} and {args['upper']} ","red"), sep = "\n")
    elif(pnrt_val == 'more'):
        print(colored("Your number is more than need, enter  number again : ", "red"))
    elif(pnrt_val == 'les'):
        print(colored("Your number is less than need, enter  number again : ", "red"))
    elif(pnrt_val == 'win'):
        print(colored(pyfiglet.figlet_format(f"Congrats, you are guessed the number {int_num} !!!!",width = 180), "yellow"))
    else :
        print(colored(pyfiglet.figlet_format(f"Hello Player , enter your number between   {args['lower']}  and  {args['upper']}  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game", width = 190), "green"))

#Define function for verifying user inputed data 
def usr_inp():
    try:
        usr_inpt = input() # usr_inpt puted into try for KeyboardInterrupt catching
        if usr_inpt == 'exit':
            raise Exception ('Exit')
        usr_inpt = int(usr_inpt)
    except ValueError:
        msg('wrng')
        return None
    except KeyboardInterrupt:
        raise Exception ('Exit')
    else:
        if args['lower'] <= usr_inpt <= args['upper'] :
            return usr_inpt
        else:
            msg('wrng')
            return None

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

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("-u", "--upper", required=False, default=10, type=int, help="upper border")
ap.add_argument("-l", "--lower", required=False, default=0, type=int, help="lower border")
args = vars(ap.parse_args())

int_num = random.randint(int(args['lower']), int(args['upper'])) # Generate random number
msg(0)# Print Hello message
print(int_num) # Print hint

#Main program cycle
while True:
    try:
        user_inpt = usr_inp()fffff
    except Exception:
        msg('exit')
        break
    else:
        try:
            game_cnd(user_inpt)
        except Wrng_exception :
            continue
        except Win_exception:
            time.sleep(5)
            break

