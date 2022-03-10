import argparse
from dataclasses import replace
from termcolor import colored

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("-p", "--pattern", required=True,  type=str, help="please enter searching value")
ap.add_argument("-f", "--file", required=True,  type=str, help=r"C:\txt1.txt")
ap.add_argument("-c", "--color", required=False,  type=str, help=r"colors (yellow,red,blue)", default="yellow")
args = vars(ap.parse_args())

def ptrn_marker(orig_line):
    orig_line = ''.join(orig_line)
    orig_line=orig_line.replace(args['pattern'],colored(args['pattern'],args['color']))
    return orig_line

def line_parse(text):
    ptrn_math=[]
    for sngl_line in text:
        if args['pattern'] in sngl_line:
             ptrn_math.append(sngl_line)
    print(ptrn_marker(ptrn_math))
    
try:
    with open(args['file'],'r') as r_file:
        t_file = r_file.readlines()
except FileNotFoundError:
    print(colored("File not found, please enter existing file name with file path", "red"))
else:
    line_parse(t_file)
