import cv2 as cv
import numpy as np
import math

window1 = "OpenCV_Logo"
cv.namedWindow(window1, cv.WINDOW_AUTOSIZE)
screen_x, screen_y = 512, 512
logo_size = 60
screen = np.zeros((screen_y, screen_x, 3), np.uint8)

def triangel_point(screen_x, screen_y, triangle_length):
    center_x, center_y = screen_x//2, screen_y//2
    
    height = (math.sqrt(3)/2)*triangle_length
    
    upper_point = (center_x, int(center_y - (2/3)*height))
    left_point = (int(center_x - triangle_length/2), int(center_y + (1/3)*height))
    right_point = (int(center_x + triangle_length/2), int(center_y + (1/3)*height))
    
    return [upper_point, left_point, right_point]

def drawing_logo(x, y, size, color):
    # red
    if color == "red":
        cv.ellipse(screen, (x, y), (size, size), 120,0,300,(0,0,255),-1)
        cv.ellipse(screen, (x, y), (size//3, size//3), 120,0,300,(0,0,0),-1)

    # green
    if color == "green":
        cv.ellipse(screen, (x, y), (size, size), 0,0,300,(0,255,0),-1)
        cv.ellipse(screen, (x, y), (size//3, size//3), 0,0,300,(0,0,0),-1)

    # blue
    if color == "blue":
        cv.ellipse(screen, (x, y), (size, size), 300,0,300,(255,0,0),-1)
        cv.ellipse(screen, (x, y), (size//3, size//3), 300,0,300,(0,0,0),-1)
        

upper_point, left_point, right_point = triangel_point(screen_x, screen_y, 130)
drawing_logo(upper_point[0], upper_point[1], logo_size, "red")
drawing_logo(left_point[0], left_point[1], logo_size, "green")
drawing_logo(right_point[0], right_point[1], logo_size, "blue")

cv.imshow(window1, screen)
cv.moveWindow(window1, 1400, 300)
cv.waitKey(0)