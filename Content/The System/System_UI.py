# Name:         System_Recognizer
# Supervisor:   Prof. P Wentworth
# Authors:      MS Kingon, M Lorenco
# Description:  File Contaiing support functions for the cmd prompt UI
# ============================================================================ #
# import relevant files
import cv2
import numpy as np
import os
from os.path import isdir, join

def Initilise_UI():
    # initilises aspects of the user interface
    os.system('cls');                                                           # Clean window for new UI


def topStructure_UI():
    # ask client if they would like to simply use default settings
    os.system('cls');                                                           # Clean window for new UI
    print("------------------------------ ------------------------------");
    print("Welcome to the Facial Identification and recognition tool-kit");
    print("The only recognized commands are numerical.  Please refer to \non-screen aid to help decide which number to use.\n");
    print("Authors: \n---------")
    print("   Peter Wentworth   - (supervisor, Logistics)\n   Marcelo Lourenco  - (Face identification)\n   Matthew S. Kingon - (Face recognition)");

def Mainmenu_UI():
    # UI for the main menu
    topStructure_UI()                                                           # setup new UI window
    print("------------------------------ ------------------------------");
    print("Are you:");
    print("------------------------------ ------------------------------");
    print("0 - <Using> --------------------! ");                                #
    print("1 - <Training>");                                                    # implment a system to save the recognizer object to a file
    print("2 - <Train then use>")                                               # hence allowing the user to immideatly choose "Using"
    u = input();

    topStructure_UI();
    print("------------------------------ ------------------------------");
    print("Would you like to:");
    print("------------------------------ ------------------------------");
    print("0 - <do no pre-proccessing>");
    print("1 - <perform pre-proccessing>");
    p = input();

    if p == 1:
        topStructure_UI()
        print("------------------------------ ------------------------------");
        print("Would you like to:");
        print("------------------------------ ------------------------------");
        print("0 - <use default parameters>");
        print("1 - <manually assign settings> --------------------!");
        if input():
            return u, p, Config_UI();

    return u, p, Set_defaults();

def Config_UI():
    # allows user to config settings to be used by the identifier and recognizer
    # defaults:
    #
    #
    #
    #
    topStructure_UI()                                                           # setup new UI window
    print("------------------------------ ------------------------------");
    return Set_defaults();

def Firsttime_UI():
    topStructure_UI();
    print("------------------------------ ------------------------------");
    print("Would you like to skip setup and use Default settings?")
    print("------------------------------ ------------------------------");
    print("0 - <No>");
    print("1 - <Yes>");
    return input();

def Set_defaults():
    return [0,0,0,0,0,0,0,0,0,0];