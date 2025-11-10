import cv2 as cv
import numpy as np

window1 = "Window1"
cv.namedWindow(window1, cv.WINDOW_AUTOSIZE)

# img = np.zeros((400, 600, 3), np.uint8)
img = np.full((400, 600, 3), 0, dtype=np.uint8)
cv.imshow(window1, img)
cv.moveWindow(window1, 1400, 400)

""" def onChange(x):
    global img
    print(f"Trackbar Value: {x}")
    img[:] = (x, x, x)
    cv.imshow(window1, img)

cv.createTrackbar("Brightness", window1, 0, 255, onChange) """

point1, point2 = (50, 50), (550, 350)
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)

def line_draw(event, x, y, flags, param):
    global point1, point2
    if event == cv.EVENT_LBUTTONDOWN:
        point1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON):
        img_copy = img.copy()
        point2 = (x, y)
        cv.rectangle(img_copy, point1, point2, green, thickness=3)
        cv.imshow(window1, img)
    elif event == cv.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv.rectangle(img, point1, point2, green, thickness=3)
        cv.imshow(window1, img)
        
cv.setMouseCallback(window1, line_draw, param=".")   
cv.waitKey(0)