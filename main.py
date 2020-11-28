import cv2
import numpy as np
import pyautogui
from pynput.keyboard import Listener

def on_press(key):
    if str(key) == '\'q\'':
        Rec()
    pass

def on_release(key):
    pass

def Rec():
    while True:
        print("rec")
        # make a screenshot
        img = pyautogui.screenshot()
        # img = pyautogui.screenshot(region=(0, 0, 300, 400))
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        # cv2.imshow("screenshot", frame)
        # if the user clicks q, it exits
        # print(img)


print("import ok")

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    with Listener(on_press=on_press) as listener:
        listener.join()


# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()