## Homework - Rotating an Image
## COMP 350 
## by Sabrina Galban
## This python program will read an image, create a tuple from the center of the
## image, create the rotation matrix, then finally display the rotated image.
import cv2  
import numpy as np
 
# read an image as input using OpenCV
image = cv2.imread('illusion.jpg')
angle = 180

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    
    # displays non-rotated image 
    cv2.imshow("Non-Rotated Image", image)
    cv2.waitKey(0)
    
    # displays rotated image
    cv2.imshow("Rotated Image", result)
    cv2.waitKey(0)
    
    return result

rotate_image(image, angle)
