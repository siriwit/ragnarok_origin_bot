from windows_capture import WindowCapture
import cv2 as cv
from search_screen import *
from click import *
import time
import img
import utils
import sys

window_name = 'LDPlayer'
window = WindowCapture(window_name)
 ## check click hwid
myclick = Click(window_name)
hwid = myclick.gethwid()

offset_x = 100
offset_y = 45

while True:
    #take sceenshot
    image_obj = utils.find_image_with_similarity(img.boss_angeling)
    screenshot = window.screenshot()
    if image_obj is not None:
        x, y, width, height = image_obj
        x1 = (x + offset_x)
        y1 = (y + offset_y)
        x2 = (x1 + width - offset_x)
        y2 = (y1 + height)
        roi = screenshot[y1:y2, x1:x2]
        cv.imwrite('cropped_image.png', roi)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            sys.exit(0)


