# Name:         System_Recognizer
# Supervisor:   Prof. P Wentworth
# Authors:      MS Kingon, M Lorenco
# Description:  File containing main method that takes a set of faces and
#               determines who they are.
# ============================================================================ #
# import relevant files
import cv2
import numpy as np
import os
from os.path import isdir, join

# globals (the recognizer)
Garrus = cv2.createEigenFaceRecognizer();

def Recognize_train(training_set):
    # trains the system with the data provided, will return the mean face that is created.
    xlabels = []; xtemp = []; train_set = [];
    ave_face = [[0 for col in range(112)] for row in range(148)]
    # set up the traning data from imported images
    mean = [[0 for x in range(112)] for y in range(148)]

    for i in range(0, len(training_set)):
        for k in range (1, len(training_set[i])):
            xtemp.append(training_set[i][0]);
            train_set.append(np.asarray(training_set[i][k], dtype=np.uint8));
            mean += training_set[i][k]

    mean = mean/len(training_set);
    img_out = np.matrix(mean, np.uint8);

    # let the traning commence!
    xlabels = np.asarray(xtemp, dtype = np.int32);
    Garrus.train(train_set, xlabels);
    return img_out;

def Recognize_main(face_set):
    # main function for recognizer takes as input an input set of faces and
    # compares them against a known database.  outputs ...
    for i in range(0, len(face_set)):
        for k in range(1, len(face_set[i])):
            [p_label, p_confidence] = Garrus.predict(np.asarray(face_set[i][k], dtype=np.uint8))
            print("This is {0},  of which we get a score of: {1}.\n".format(p_label, p_confidence));
    return None;

def Recognize_import(path):
    # import function for recognizer, takes the files created by the detector
    # componenets and puts the frames into an array.
    # it expects the file structure to be a outer directory within lies sub
    # folders per studant within each can be a variable No. of photos.

    # input:    folder to fetch from.
    # output:   Array of arrays, starting with std. No. and one or more images
    #           for that person.

    paths = cats_and_subs(path)
    out = [None]*len(paths);

    for i in range(0, len(paths)):
        dirlist = os.listdir(paths[i])
        out[i] = [int(dirlist[0][:2] + dirlist[0][3:7])];
        for f in dirlist:
            out[i].append(cv2.resize(cv2.imread(paths[i] + f, 0),(112,148)));

    return out;

def cats_and_subs(pth):
    # traverse the file system to find needed paths to images
    cats = []; subcats = [];  paths = [];
    for (dirpath, dirnames, filenames) in os.walk(pth):
        if (dirpath == pth):
            cats = dirnames;
        else:
            subcats.extend(dirnames);
            dirnames[:]=[];  # don't walk any further downwards

    # create a list of paths
    for i in range(0, len(subcats)):
        paths.append(pth + '/' + cats[0] + '/' + subcats[i] + '/');

    if (len(subcats) == 0):
        paths = [pth + '/' + cats[0] + '/'];

    return (paths);

