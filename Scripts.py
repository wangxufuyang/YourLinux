#!/usr/bin/python3

import os
import sys


IPDevice = []
Directory = '/usr/local/scripts'


'''
 _     Start banner                            
| |                                
| |__   __ _ _ __  _ __   ___ _ __ 
| '_ \ / _` | '_ \| '_ \ / _ \ '__|
| |_) | (_| | | | | | | |  __/ |   
|_.__/ \__,_|_| |_|_| |_|\___|_|   
'''
def Banner():
    print("\033[1;96m     Author: TEAM003\033[91m")
    print("      ___           ___           ___                       ___                     ___      ")     
    print("     /  /\         /  /\         /  /\        ___          /  /\        ___        /  /\     ")
    print("    /  /:/_       /  /:/        /  /::\      /  /\        /  /::\      /  /\      /  /:/_    ")
    print("   /  /:/ /\     /  /:/        /  /:/\:\    /  /:/       /  /:/\:\    /  /:/     /  /:/ /\   ")
    print("  /  /:/ /::\   /  /:/  ___   /  /:/~/:/   /__/::\      /  /:/~/:/   /  /:/     /  /:/ /::\  ")
    print(" /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/   /  /::\    /__/:/ /:/\:\ ")
    print(" \  \:\/:/~/:/ \  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/   /__/:/\:\   \  \:\/:/~/:/ ")
    print("  \  \::/ /:/   \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/    \__\/  \:\   \  \::/ /:/  ")
    print("   \__\/ /:/     \  \:\/:/     \  \:\          /__/:/    \  \:\         \  \:\   \__\/ /:/   ")
    print("     /__/:/       \  \::/       \  \:\         \__\/      \  \:\         \__\/     /__/:/    ")
    print("     \__\/         \__\/         \__\/                     \__\/                   \__\/     ")



'''
    Check if there are relevant permissions
'''
def CheckPermissions():
    # Check if there are relevant permissions          
    if os.getuid() != 0:
        print("\033[7;91mERROR: You must not run Script as root!\033[0m")
        sys.exit(1)



'''
    Delete the Script folder and create a new one
'''
def DNFolder():
    # Delete the Script folder and create a new one
    if os.path.exists(Directory):
        print(f"\033[1;91mThe {Directory} folder exists, should it be deleted?\033[0m")
        flag = True
        while flag:
            yn = input("\033[93mY/N: \033[0m")
            if 'N' == yn or 'n' == yn:
                print("\033[1;91mThanks, Please delete the folder and try running the program again.\033[0m")
                sys.exit(0)
            elif 'Y' == yn or 'y' == yn:
                if 0 == os.system(f"rm -r {Directory}"):
                    print("\033[1;92mDelete successfully\033[0m")
                flag = False
            else:
                print(f"\033[1;91mPlease enter Y or N\033[0m")
               
    if  False == os.path.exists(Directory):
        print(f"\033[1;91m{Directory} does not exist. Do you want to create a new one?\033[0m")
        flag = True
        while flag:
            yn = input("\033[93mY/N: \033[0m")
            if 'N' == yn or 'n' == yn:
                print(f"\033[1;91mEnd of program, please create a  {Directory} folder\033[0m")
                sys.exit(0)
            elif 'Y' == yn or 'y' == yn: 
                if 0 == os.system(f"mkdir {Directory}"):
                    print("\033[1;92mNew folder successfully\033[0m")
                flag = False
            else:
                print(f"\033[1;91mPlease enter Y or N\033[0m")



'''
    Get the network card name
'''
def GetNetwork():
    global IPDevice
    IPDevice = os.popen("ip link | grep -E '^[0-9]' | awk -F: '{print $2}' | sed s/[[:space:]]//g").read().splitlines()

'''
    Add environment variables for all users
'''
def EVar():
    print("\033[1;91mPlease set environment variables yourself.\033[0m")
    

def Initialization():
    CheckPermissions()
    DNFolder()
    GetNetwork()
   
   
    
def script_stencil(FileName, Script):
    f = open(f"{Directory}/{FileName}",'a')
    f.write("#!/bin/bash")
    f.write("\n")
    f.write(f"{Script}")
    f.close()
    
   

def Scripts():
    i()
    i2()



def End():
    # Grant script permissions
    os.system(f"chmod +x {Directory}/*")
    
    EVar()


# 
def i():
    for ipdev in IPDevice:
        # print(ipdev)
        # print(f"ip addr show dev {ipdev} " + "| grep 'inet ' | awk -F ' ' '{print $2}' | awk -F '/' '{print $1}'")
        script_stencil(ipdev, f"ip addr show dev {ipdev} " + "| grep 'inet ' | awk -F ' ' '{print $2}' | awk -F '/' '{print $1}'")



def i2():
    for ipdev in IPDevice:
        # print(ipdev)
        # print(f"ip addr show dev {ipdev} " + "| grep 'inet ' | awk -F ' ' '{print $2}'")
        script_stencil(ipdev + "2", f"ip addr show dev {ipdev} " + "| grep 'inet ' | awk -F ' ' '{print $2}'")



if __name__ == "__main__":
    # Start banner
    Banner()
    
    # Initialization
    Initialization()
    
    # Script
    Scripts()
    
    # End Work
    End()
    # test function 
    
