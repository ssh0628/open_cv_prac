import cv2 as cv

window1 = "First Window"
window2 = "Second Window"
cv.namedWindow(window1, cv.WINDOW_NORMAL)
cv.namedWindow(window2, cv.WINDOW_AUTOSIZE)

image_path = "cat.png"
img = cv.imread(image_path)

cv.imshow(window1, img)
cv.moveWindow(window1, 1400, 300)
# cv.imshow(window2, img)
# cv.moveWindow(winname=window2, x=1400, y=600)


clicked = False
def printMouseEvent(event, x, y, flags, param):
    global clicked
    if event == cv.EVENT_LBUTTONDOWN:
        clicked = True
    if event == cv.EVENT_MOUSEMOVE:
        if clicked:
            img[y, x] = (255, 0, 0)
            cv.imshow(window1, img)
    if event == cv.EVENT_LBUTTONUP:
        clicked = False
        

cv.setMouseCallback(window1, printMouseEvent, param="Hello")

cv.waitKey(0)
""" while True:
    key = cv.waitKey(100)
    if key == ord('q'):
        break """