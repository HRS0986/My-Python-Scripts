#! python3
# TakeSS - Simple screen capturing tool
# Developed By Hirusha Fernando

from pyscreenshot import grab 
from datetime import datetime
from colorama import Fore,init
import argparse as ap
import time, os, platform, sys


# Usage : takess PATH [-d D] [-b X1 Y1 X2 Y2] [-f GAP FC | -w WD WC] [-i] [-h]

# DEFAULT SAVE NAME FORMAT = dd/mm/yy/SS/MM/HH => 200521453217
# 20-05-23 16:57:06

# Initialize colorama module
init()

# Check what is the running OS
OS = platform.system()

def captureScreen(pathT, delay ,box, x1, y1, x2, y2, fmode ,gap, fc, wmode, wd, wc, isHide):
    
    '''
    This function captures the screenshot
   
    params:
        pathT : path to save screenshot and default path status. Tuple value

        delay : delay to start TakeSS in seconds. Integer value   

        box : set custome screenshot coordinates. Boolean Value
            X1,Y1 : starting coordinates. Both are integer values
            X2,Y2 : ending coordinates. Both are integer values
        
        fmode : set the for loop mode. Boolean Value
            gap : delay between two screenshots. Integer value
            fc : number of screenshots to capture. Integer value

        wmode : set the while loop mode. Boolean Value
            wd : duration to take screenshots. Integer value
            wc : number of screenshots to capture within duration. Integer value

        isHide : Screenshot hide status. Boolean value

    '''
    # Extract path and defaultPath status
    path, isDefaultPath = pathT[0], pathT[1]
    
    try:
        # Path verifying part
        if not isDefaultPath:
            # Get the folder path from full save path
            pathTemp = str(str(path[::-1])[path[::-1].index('\\'):])[::-1]
            # Verify the path
            isPathValid = os.path.exists(pathTemp)
            # Invalid Path Error
            if not isPathValid:
                print(Fore.RED + 'TakeSS: Path is not valid')
                sys.exit(1)
    except ValueError:
        print(Fore.RED + 'TakeSS: Path is not valid')
        sys.exit(1)

    # Delay specific seconds
    time.sleep(delay)

    # Delay between two screenshots
    delayBetweenSS = 0.0

    # Screenshots count.
    ssCount = 1

    # Check loop mode
    if fmode:
        delayBetweenSS = gap
        ssCount = fc
    elif wmode:
        delayBetweenSS = wd / wc
        ssCount = wc

    # Screen capturing part
    for shot in range(ssCount):
        
        ss = grab(bbox=(x1,y1,x2,y2))
        # Save Screenshot
        ss.save(path)

        # OS based screenshot hide process
        if isHide:
            if OS == 'Windows':
                os.system(f"attrib +h +s {path}")
            elif OS == 'Linux':
                os.system(f'mv {path} .{path}')
        
        # Waiting for capture next screenshot
        time.sleep(delayBetweenSS)
    
    if not isHide:
        print(Fore.GREEN + f'TakeSS: Screenshot saved in {path}')
    sys.exit(1)

def defaultName():
    
    '''
    This function create the default savefile name for the screenshot.
    If user didn't give the save path this function will be called.If
    user didn't give the save path screenshot saved in current directory.

    Default Save Name Format = yymmddSSMMHH
    Ex:- 201203564317.png, 
         201103564303.jpg
    
    '''

    DATE = ''.join(str(datetime.now())[2:10].split('-'))    # string
    TIME = ''.join(str(datetime.now())[11:19].split(':'))   # string
    FILENAME = f'{DATE}{TIME}.png'
    return (FILENAME,True)
    
