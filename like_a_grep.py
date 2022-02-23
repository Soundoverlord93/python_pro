import argparse
from termcolor import colored

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("-p", "--pattern", required=True,  type=str, help="please enter searching value")
ap.add_argument("-f", "--file", required=True,  type=str, help=r"C:\txt1.txt")
args = vars(ap.parse_args())


try:
    t_file = open(args['file'])
except FileNotFoundError:
    print(colored("File not found, please enter existing file name with file path", "red"))
else:
    f_data = t_file.readlines()
    for f_line in f_data:
        if args['pattern'] in f_line:
            f_line = f_line.replace(args['pattern'],colored(args['pattern'],"yellow"))
            print (f"{f_line}")

