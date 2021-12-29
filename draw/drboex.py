# from PIL import Image
import argparse
import os
import sys
import cv2
import numpy as np
import math
import json
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
def draw_ocr_box_txt(image,
                     boxes):
    h, w = image.height, image.width
    img_left = image.copy()

    import random
    random.seed(0)
    draw_left = ImageDraw.Draw(img_left)
    for idx, box in enumerate(boxes):

        color = (random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255))
        draw_left.polygon(box, fill=color)
        # box_height = math.sqrt((box[0][0] - box[3][0])**2 + (box[0][1] - box[3][
        #     1])**2)
        # box_width = math.sqrt((box[0][0] - box[1][0])**2 + (box[0][1] - box[1][
        #     1])**2)
        #
    img_left = Image.blend(image, img_left, 0.5)
    img_r=np.array(img_left)
    plt.imshow(img_r)
    plt.show()
def main():
    path2="./test"
    path1="./labels"
    dirs=os.listdir(path2)
    for i in dirs:
        m=os.path.join(path2,i)
        img=Image.open(m)
        # img=np.array(img)
        # f=open(os.path.join(path1,i+".txt"))
        # lines=f.readlines()
        boxes=[]
        with open(os.path.join(path1,i+".txt"),encoding="utf8") as f:
            lines=f.readlines()
            for line in lines:
                line=line.split(",")
                bx=[]
                for j in range(0,8,1):
                    bx.append(int(line[j]))
                boxes.append(bx)
        draw_ocr_box_txt(img,boxes)
if __name__ == '__main__':
    main()
    # return np.array(img_show)