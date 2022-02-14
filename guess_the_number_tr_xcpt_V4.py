import random
import pyfiglet
from termcolor import colored
# Define print function for user interactivity 
def prnt(pnrt_val) :
    if pnrt_val == 'exit' :
        print(colored(pyfiglet.figlet_format("Goodbye !!!"), "green"))
    elif(pnrt_val == 'wrng'):
        print("Wrong value entered, please enter  number between 0 and 10 ", sep = "\n")
    elif(pnrt_val == 'more'):
        print(colored("Your number is more than need, enter  number again : ", "red"))
    elif(pnrt_val == 'les'):
        print(colored("Your number is less than need, enter  number again : ", "red"))
    elif(pnrt_val == 'win'):
        print(colored(pyfiglet.figlet_format(f"Congrats, you are guessed the number {int_num} !!!!",width = 180), "yellow"))
    else :
        print(colored(pyfiglet.figlet_format("Hello Player , enter your number between   0  and  10  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game", width = 190), "green"))
int_num = random.randint(0, 10) # Generate random number
prnt(0) # Print Hello text
print("hint for test : ", int_num) # Hint for testing program
# Game core
while True :
    wrng = None
    int_usr_num = input()
    try:
        int_usr_num = int(int_usr_num)
    except ValueError : # Catch wrong input value 
        if int_usr_num == "exit" :
            prnt(int_usr_num)
            break
        wrng = 'wrng'
        prnt(wrng)
    except KeyboardInterrupt: # Intercept keyboard  interrupt
        prnt(int_usr_num)
        break
    else: # main game conditions 
        if int_usr_num <= 10 or int_usr_num <= 0:
            if int_usr_num > int_num:
                wrng = 'more'
                prnt(wrng)
            elif int_usr_num < int_num:
                wrng = 'les'
                prnt(wrng)
            else:
                wrng = 'win'
                prnt(wrng)
                break
        else:
            wrng = 'wrng'
        prnt(wrng)


"""
Использовал функцию только для вывода сообщений поскольку не знаю что можно было бы улучшить ( рандом и так лаконичен и вызивается только раз) разве что, всю игру в функцию загнать

"""