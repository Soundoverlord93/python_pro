import random
import pyfiglet
from termcolor import colored

int_num = random.randrange(0, 10)
print("hint for test : ", int_num)
int_usr_num = None
print(colored(pyfiglet.figlet_format("Hello Player , enter your number between   0  and  10  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game", width = 200), "green"))
while True :
    try:
        int_usr_num = input()
        int_usr_num = int(int_usr_num)
    except ValueError :
        if int_usr_num == "exit" :
            print(colored(pyfiglet.figlet_format("Goodbye !!!"), "green"))
            break
        print("Wrong value entered, please enter  number between 0 and 10 ", sep = "\n")
    except KeyboardInterrupt:
        print(colored(pyfiglet.figlet_format("Goodbye !!!"), "green"))
        break
    else:
        if int_usr_num <= 10 or int_usr_num <= 0:
            if int_usr_num > int_num:
                print(colored("Your number is more than need, enter  number again : ", "red"))
            elif int_usr_num < int_num:
                print(colored("Your number is less than need, enter  number again : ", "red"))
            else:
                win_cn='Congrats, you are guessed the number ', int_num,'!!!!'
                print(colored(pyfiglet.figlet_format(str(win_cn),width = 180), "yellow"))
                break
        else:
            print(colored("Wrong number, please enter  number between 0 and 10 again : ", "red")) 

