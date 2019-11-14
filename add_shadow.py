import cv2
import numpy as np
import random

def add_shadow(img_url):
    orimg = cv2.imread(img_url,cv2.IMREAD_GRAYSCALE)
    maskurl = "mask/"+str(int(random.random()*10))+".png"
    maskimg = cv2.imread(maskurl,cv2.IMREAD_GRAYSCALE)

    orimg_resize = cv2.resize(orimg,(256,256))
    maskimg_resize= cv2.resize(maskimg,(256,256))

    # mask = np.zeros([258,258],np.uint8)
    # cv2.floodFill(orimg_resize,mask,(1,1),255,100,0)
    # mask = mask[1:257,1:257]
    # cv2 .namedWindow("input image",cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("temp result",mask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # mask_no = cv2.bitwise_not(mask)
    # maskimg_resize = cv2.bitwise_and(mask_no,maskimg_resize)


    resultimg = cv2.bitwise_and(orimg_resize,maskimg_resize)
    cv2 .namedWindow("input image",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("temp result",resultimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    add_shadow("data/test2.png")