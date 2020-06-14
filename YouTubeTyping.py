# Youtube Typing
# By Hirusha Fernando

'''

This script is for youtubers who type what they do in notepad.
You can insert things to text file that you want to show in video 
including specific color. Give the path of text file. Text file 
should be like this
    
    ##COLOR@@YourText
    ##COLOR@@YourText
    YourText

Example:-
        ##RED@@This is a testing text
        ##GREEN@@This is line two
        This is line 3
        ##YELLOW@@This is line 4
        ##RED@@This is last line

Available Colors: RED, GREEN, YELLOW, BLUE, CYAN, MAGENTA, BLACK, WHITE

Run this script and start recording your video 
This script will display line by line in the text file when you press enter

'''

from time import sleep
from os import system
from colorama import init, Fore

# initialize the colorama module
init(convert=True)

# Get the text file location and format path
path = '\\\\'.join(input('Enter text file path: ').strip().split('\\'))

# clear the terminal window
system('cls')

# leave a blank line
print()

# variables to store color and starting index
clr, ind = '', 0

# read the text file and print line by line
with open(path, 'r') as file:

    # Read line by line in text
    for line in file:
        
        # Check the line color
        if line[:2] == '##':

            # Extract the color from line
            clr = 'Fore.'+line[2:line.index('@@')]
            
            # Set the starting index to print 
            ind = line.index('@@')+2

            # Set the color of the line
            exec(f"print({clr}, end='')")
        
        # Print letter by letter in the line
        for letter in line[ind:]:
            print(letter, end='', flush=True)
            sleep(0.05)
        
        # Reset the terminal color to default
        print(Fore.RESET)

        # set the starting index to zero 
        ind = 0

        # Wait for the user's command to print next line
        system('pause > nul')

