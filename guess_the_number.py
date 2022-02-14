int_num0 = 3
int_input_num = None
str_chk = 0
print("Hi player, enter your number between 0 and 10 here or type exit to stop game : ")

while int_input_num is not int_num0 and str_chk != "exit" :
    str_chk = input()
    if str_chk != "exit" and  str_chk.lstrip('-').isdigit():
        int_input_num = int(str_chk)
        if int_input_num > 10 or int_input_num < 0:
            print("Wrong number, please enter  number between 0 and 10 again : ")
        else:
            if int_input_num > int_num0 :
                print("Your number is more than need, enter  number again : ")
            elif int_input_num < int_num0:
                print("Your number is less than need, enter  number again : ")
            else:
                print("Congrats, you are guessed the number ", int_num0,"!!!!")
                break
    elif str_chk == "exit" : 
        print("You got out of the game ")
        break
    else :
        print("Wrong input")