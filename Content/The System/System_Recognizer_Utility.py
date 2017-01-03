# Name:         System_Recognizer_Utility
# Supervisor:   Prof. P Wentworth
# Authors:      MS Kingon, M Lorenco
# Description:  A File acting as a library containing various recognizer
#               specific functions for the system
# ============================================================================ #
import cv2
import numpy as np

def Export_single(img, file_name):
    # exports a single image to a specified file name
    # exports as .png
    cv2.imwrite(file_name + '.png', img);

def Export_mult(img_arry, file_name):
    # takes an array of images and exports them to a specified file
    # exports as .png
    # ensures all possible cases are handled (1 img, or more than 1)
    if(len(img_arry) <= 1):
        print('Please use "Export_single" for single images.');

    # fetch the images width and height
    h, w = img_arry[0][1].shape[:2]

    # construct the bounds of the output image
    h_out = h*(int(len(img_arry)/4));
    w_out = w*4
    img_out_build = np.zeros((h_out, w_out), np.uint8);

    # loop through all images and add them to the output image
    h_comp, w_comp = 0, 0;
    for i in range(0, len(img_arry)):
        # add the next image into its slot.
        img_out_build[(h_comp*h):h+(h_comp*h), (w_comp*w):w+(w_comp*w)] = (img_arry[i][1]);
        w_comp +=1 ;

        # loop maintanance (ensure we add the image correctly)
        if ((i+1) % 4 == 0):
            w_comp  = 0;
            h_comp += 1;

    cv2.imwrite(file_name + '.png', img_out_build);

# ============================================================================ #
def Display_single(img):
    cv2.imshow('image:', img);
    cv2.waitKey(0);
    cv2.destroyAllWindows();
    return None;

def Display_mult(img_arry):
    # takes an array of images and displays them (for code testing purposes.)
    # ensures all possible cases are handled (1 img, or more than 1)
    if(len(img_arry) == 1):
        cv2.imshow('test image for: '+ str(img_arry[0][0]), img_arry[0][1]);
        return img_arry[0][1];
    elif(len(img_arry) < 1):
        return None;

    # fetch the images width and height
    h, w = img_arry[0][1].shape[:2]

    # construct the bounds of the output image
    h_out = h*(int(len(img_arry)/4));
    w_out = w*4
    img_out_build = np.zeros((h_out, w_out), np.uint8);

    # loop through all images and add them to the output image
    h_comp, w_comp = 0, 0;
    for i in range(0, len(img_arry)):
        # add the next image into its slot.
        img_out_build[(h_comp*h):h+(h_comp*h), (w_comp*w):w+(w_comp*w)] = (img_arry[i][1]);
        w_comp +=1 ;

        # loop maintanance (ensure we add the image correctly)
        if ((i+1) % 4 == 0):
            w_comp  = 0;
            h_comp += 1;

    # construct the new opencv image from the compiled image data
    cv2.imshow('Set:', img_out_build);
    cv2.waitKey(0);
    cv2.destroyAllWindows();

    return img_out_build;
# ============================================================================ #

def Ghost(img_arry, mean):
    # takes an input array of images and subtracts each from the mean image
    ghost_arry = [None]*len(img_arry);

    for i in range(0, len(img_arry)):
        ghost_arry[i] = [img_arry[i][0]];
        ghost_arry[i].append(img_arry[i][1] - mean);


    return ghost_arry;