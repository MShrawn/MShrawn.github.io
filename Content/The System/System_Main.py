# Name:         System_Main
# Supervisor:   Prof. P Wentworth
# Authors:      MS. Kingon, M. Lorenco
# Description:  Main File for class attendance traking system.  Acts as the main
#               scaffolding between the various componenets of the system.
# ============================================================================ #

# import functions from the three componenets
# import from detector

import os;
from System_UI import *
from System_Recognizer import *

# import from logistics

# Flags
skip_setup = False;     # does client wish to skip setup (use default or last predifined settings)


def perform_operation(args):
    # args contains the user defined argument choices:
    # please refer above for symbol meaning.
    # args[0] - u
    # args[1] - p
    # args[2] -
    # args[3] -
    # args[4] -
    # args[5] -
    # args[6] -

    # ============================================================================ #
    # Marcelo section:
    # ============================================================================ #
    # collect faces from the face detection+tracking system.

    # ============================================================================ #
    # Matthew Section:
    # ============================================================================ #
    # fetch test and actual data from file and pass these faces into our Recognizer
    # for training and reconition respectfully.
    # read data in
    in_test_set = Recognize_import('Test_data_00');
    in_face_set = Recognize_import('Detector_out');

    # do we perform pre-proccessing?
    if args[1] == 1:
        # perform pre-proccessing
        pass;

    # are we training or not or both?
    if args[0] == 2:
        mean = Recognize_train(in_test_set);       # train the recognizer
        Recognize_main(in_face_set);
    elif args[0] == 1:
        mean = Recognize_train(in_test_set);       # train the recognizer
    else:
        Recognize_main(in_face_set);

    # ============================================================================ #
    # Prof. Wentworth section *
    # ============================================================================ #
    # import results from file and pass these results to logistics componenet


# main running loop
while True:
    # this always runs repeatadly waiting for user input
    # description of user defined Data:
    # status    - indicates weather the user would like to start again or quit the session
    # u         - is there training?
    # p         - is there pre-proccessing?

    # pre cycle clean up
    os.system('cls')

    if skip_setup == False:
        skip_setup = Firsttime_UI();

        if skip_setup == 1:
            u, p, config_settings = 2, 1, Set_defaults();                                              # Assign default values
        else:
            u, p, config_settings = Mainmenu_UI();                                                     # display Main menu

    # run recognition with predifined user settings
    perform_operation([u, p]);

    # what does the user wish to do upon compleation?
    skip_setup = False; # clean for next use.
    print("------------------------------ ------------------------------");
    print("Work complete, Would you like to:")
    print("------------------------------ ------------------------------");
    print("0 - <re-run>");
    print("1 - <Edit settings>");
    print("2 - <quit>")

    status = input();
    if status == 2:
        os.system('cls');
        break;
    elif status == 1:
        pass;
    else:
        skip_setup = True;


