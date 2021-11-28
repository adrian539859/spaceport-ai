import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def label_func(x): return x.parent.name
learn_inf = load_learner("data/export.pkl")
print("loaded model")

# Sleep time after actions
sleepy = 0

# Wait for me to push B to start.
keyboard.wait('O')
time.sleep(sleepy)


while True:

    image = grab_screen(region=(394, 612, 638, 915))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    image = cv2.resize(image,(224,224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    # print(action)
    # print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())
  
    if action == "A" :
        print(f"Press A")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("space")
        
        keyboard.press("a")
        time.sleep(sleepy)

    elif action == "S" :
        print(f"Press S")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("space")
        
        keyboard.press("s")
        time.sleep(sleepy)

    elif action == "D" :
        print(f"Press D")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("w")
        keyboard.release("space")
        
        keyboard.press("d")
        time.sleep(sleepy)

    elif action == "W" :
        print(f"Press W")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.release("space")
        
        keyboard.press("w")
        time.sleep(sleepy)

    elif action == "Nothing" :
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.release("w")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Space" :
        print(f"Press Space")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.release("w")

        keyboard.press("space")
        time.sleep(sleepy)
    # End simulation by hitting h
    keys = key_check()
    if keys == "P":
        break

# keyboard.release('W')