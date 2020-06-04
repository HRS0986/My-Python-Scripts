#! python3 
# TakeSS - Simple screen capturing tool
# Developed By Hirusha Fernando

from argparse import *
from colorama import Fore,init
from win32api import GetSystemMetrics
import methods as mt


# takess PATH [-d D] [-b X1 Y1 X2 Y2] [-f GAP FC | -w WD WC] [-i] [-h]

init(convert=True)

parser = ArgumentParser(
    description='Simple Screen Capturing Tool', 
    prog='TakeSS',
    usage= '%(prog)s PATH [-d D] [-b X1 Y1 X2 Y2] [-f GAP FC | -w WD WC] [-i] [-h]',
    epilog='Developed By Hirusha Fernando'
    )

# Save path argv
parser.add_argument(
    'PATH', 
    help='Save path of screenshot', 
    type=str, 
    nargs='?'
    )

# Delay argv. Delay to start TakeSS
parser.add_argument(
    '-d', 
    help='Delay to start TakeSS', 
    type=int, 
    dest='D'
    )

# Custome Scrrenshot mode argv
parser.add_argument(
    '-b', 
    help='Screenshot coordinates', 
    type=int, 
    nargs=4, 
    metavar=('X1', 'Y1', 'X2', 'Y2'),
    dest='B'
    )

# Hide argv
parser.add_argument(
    '-i',
    help='Save and hide screenshot', 
    action='store_true'
    )

# Create the loop argv group
loop = parser.add_mutually_exclusive_group()

# for loop mode argv
loop.add_argument(
    '-f', 
    help='Enable for loop mode. GAP is the delay between two screenshots in seconds. FC is the screenshot count',
    nargs=2,
    metavar=('GAP','FC'),
    type=int,
    dest='F'
    )

# while loop mode argv
loop.add_argument(
    '-w', 
    help='Enable while loop mode. WD is the duration to take screenshots. WC is the screenshot count to take within duration',
    nargs=2,
    metavar=('WD','WC'),
    type=int,
    dest='W'
    )

# Get the user arguments
args = parser.parse_args()

# Variables for save argument values
delay,gap,fc,wd,wc = 0,0,1,0,1
(X1, Y1) = (0, 0)
(X2, Y2) = (GetSystemMetrics(0), GetSystemMetrics(1))
hide = flp = wlp = box = False
path = ('', False)

# Handle hide (-i) argument
hide = True if args.i else False

# Handle PATH argument
path = (str(args.PATH), False) if args.PATH else mt.defaultName()

# Handle delay (D) argument
delay = args.D if args.D else 0

# Verify For loop mode status
flp = True if args.F else False

# Handle GAP argument 
gap = args.F[0] if args.F else 0

# Handle FC argument
fc = args.F[1] if args.F else 1

# fmode values
fval = (flp, gap, fc)

# Verify While loop mode status
wlp = True if args.W else False

# Handle WD argument 
wd = args.W[0] if args.W else 0

# Handle WC argument
wc = args.W[1] if args.W else 1

# wmode values
wval = (wlp, wd, wc)

# Verify Custom screenshot status
box = True if args.B else False

# Handle starting coordinates
x1 = args.B[0] if args.B else 0
y1 = args.B[1] if args.B else 0

# Handle sending coordinates
x2 = args.B[2] if args.B else GetSystemMetrics(0)
y2 = args.B[3] if args.B else GetSystemMetrics(1)

# coordinates
coords = (x1, y1, x2, y2)

# Screen capturing part
mt.captureScreen(path, delay ,box, coords, fval, wval, hide)
