import cv2
import numpy as np
import random


def generate_mask(mask_name,prob):
    mask = np.zeros([1000,1000],np.uint8)
    for i in range(1000):
        for j in range(1000):
            rdn = random.random()
            if rdn < prob:
                mask[i][j] = 0
            else:
                mask[i][j] = 255
    mask = cv2.resize(mask,(100,100))
    cv2.imwrite(mask_name,mask)


if __name__ == "__main__":
    for i in range(10):
        generate_mask("mask/"+str(i)+".png",random.random()*0.1)