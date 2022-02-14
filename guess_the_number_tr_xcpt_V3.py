import random
import pyfiglet
from termcolor import colored

int_num = random.randrange(0, 11)
print("hint for test : ", int_num)
print(colored(pyfiglet.figlet_format("Hello Player , enter your number between   0  and  10  here  or  type ( \"exit\" or \"CTRL+C\" ) to stop game", width = 200), "green"))
while True :
    int_usr_num = input()
    try:
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

"""
# 1 
Ввод вынес за пределы try

#2 
int_usr_num = None, действительно не нужное но на этапе предыдущих версий просило  определить переменную поэтому так и осталось
Возможно можно как-то определить что эта переменная не нужна ?

#3
Импорты отделил от остального кода
Генератор случайных чисел также исправил, установил верхнюю границу равной 11,  а таже исправил условие int_usr_num < 0 на int_usr_num <= 0

#4
А вот поповоду win_cn там нужно работать с format или что-то иное или ещё что другое имели ввиду?


"""