import random
import pyfiglet
from termcolor import colored

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
    while True:
        usr_inpt = input()
        if usr_inpt == 'exit':
            raise Exception ('Exit') 
            break
        try:
            usr_inpt = int(usr_inpt)
        except ValueError:
            msg('wrng')
        except KeyboardInterrupt:
            raise Exception ('Exit') 
            break
        else:
            if usr_inpt <=10 and usr_inpt >=0:
                return usr_inpt
                break
            else:
                msg('wrng')

#Define function for main game logic
def game_cnd(usernum):
    if usernum > int_num:
        msg('more')
    elif usernum < int_num:
        msg('les')
    else:
        msg('win')
        raise Exception ('Win')

int_num = random.randint(0, 10) # Generate random number
msg(0)# Print Hello message
print(int_num) # Print hint

#Main program cycle
while True:
    try:
        user_inpt = usr_inp()
    except Exception:
        break
    else:
        try:
            game_cnd(user_inpt)
        except Exception:
            break


"""
1) Спасибо что подтолкнули к такому ришению. Я просто сначала не понял зачем нам там функции если и так все просто и хорошо на мой взгляд)))

2) Имя функции prnt изменил, wrng  - выбросил

3) Попробовал улучшить читабельность

Если есть ещё  замечания то говорите я постараюсь исправить
"""


fdgdgfd