# TakeSS

## Simple CommandLine Screenshot Capturing Tool

## Usage

      TakeSS PATH [-d D] [-b X1 Y1 X2 Y2] [-f GAP FC | -w WD WC] [-i] [-h]

## Arguments

```
PATH
      Path to save the captured screenshot. Defaul path is current directory. png and jpg are supported.

-d D
      When -d is enabled wait D time of seconds to start TakeSS.

-b X1 Y1 X2 Y2
      When -b is enabled TakeSS capture given area of screen X1, Y1 are starting point. X2, Y2 are ending point.
      Default (X1,Y1) is (0,0) and (X2,Y2) is length of screen and width of screen. 

-f GAP FC
      For loop mode. When this mode enabled TakeSS captures FC amount of screenshots. Delay between two screenshots is GAP.

-w WD WC
      While loop mode. When this mode enabled TakeSS captures WC amount of screenshots within WD duration of seconds.

-i
      When this option is enabled, hide screenshot automatically after capturing.

-h/--help
      Display help massage.
```