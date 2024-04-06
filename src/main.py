import pyautogui
import keyboard 
from PIL import Image, ImageGrab
import time 
import torch

# image capture settings
img_dim = (0, 102, 1920, 872)

# load model
model = torch.load("")


def main():

    time.sleep(3)
    while True:
        t_start = time.time()

        # exit condition
        if keyboard.is_pressed('q'): 
                break

        img = gui.screenshot(region=img_dim)
        img.save("dino.jpg")

        # filter this data however necessary

        # detect failure
        if failed:
            break
        
        # call model on input
        output = model(img)

        # perform action based on decision
        if output == 1:
            keyboard.press('up')
        elif output == 2:
            keyboard.press('down')
        else:
            pass



if __name__ == "__main__":
    main()


