import torch
import numpy as np

# train settings
num_epochs = 100
alpha = 1e-4

# image capture settings
img_dim = (0, 102, 1920, 872)

# load model
premodel = torch.load("")

def main():
    time.sleep(3)



    # training loop
    for epoch in range(num_epochs):


        imgs = []
        while True:
            t_start = time.time()

            img = gui.screenshot(region=img_dim)
            imgs.append(img)

            # filter this data however necessary

            # detect failure
            if failed:
                break
            
            # call model on input
            mini_train(img)

            # perform action based on decision
            if output == 1:
                keyboard.press('up')
            elif output == 2:
                keyboard.press('down')
            else:
                pass

        full_train(imgs)



if __name__ == "__main__":
    main()