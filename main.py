import cv2
import numpy as np
import pyautogui
import keyboard  # using module keyboard
from pynput.keyboard import Listener

print("import ok")

def on_press(key):
    global isRec
    print(key)
    if str(key) == "\'q\'":
        isRec = False
        print(isRec)

def on_release(key):
    pass

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write objectq
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

listaFrame = []

isRec = True

while isRec == True:
    if(keyboard.is_pressed('q')):
        print("ciao")
        break
    # make a screenshot
    img = pyautogui.screenshot()
    # img = pyautogui.screenshot(region=(0, 0, 300, 400))
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    print(len(listaFrame))
    if (len(listaFrame) == 600):
        listaFrame.pop(0)
        listaFrame.append(frame)
    else:
        listaFrame.append(frame)

    # out.write(frame)
    # show the frame
    # cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    # print(img)

for x in listaFrame:
    out.write(x)

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()