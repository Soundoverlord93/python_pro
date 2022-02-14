import random
int_num = random.randrange(1, 10)
print("hint for test : ", int_num)
int_usr_num = None
print("Hello Player, enter your number between 0 and 10 here or type exit to stop game")
while True :
    try:
        int_usr_num = int(input())
    except ValueError as vl_err:
        if "exit" in str(vl_err):
            break
        print("Wrong value entered, please enter  number between 0 and 10 ", vl_err, sep = "\n")
        
    else:
        if int_usr_num <= 10 or int_usr_num < 0:
            if int_usr_num > int_num:
                print("Your number is more than need, enter  number again : ")
            elif int_usr_num < int_num:
                print("Your number is less than need, enter  number again : ")
            else:
                print("Congrats, you are guessed the number ", int_num,"!!!!")
                break
        else:
            print("Wrong number, please enter  number between 0 and 10 again : ")

#1 Не знаю як перемістити print("Hello Player, enter your number between 0 and 10 here or type exit to stop game") в input() він в циклі кожного разу буде видавати вітання....
#2 З while виправив
#3 Не розумію, яку конструкцію треба використати  щоб розілити ввід і приведення до інта і щоб вийшло коротше....Можливо сикньте зразок