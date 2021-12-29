# 图片二值化
from PIL import Image
import numpy as np

img = Image.open('7_3.png')

arr=np.array(img)
rgb=arr.mean(axis=1).mean(axis=0)
tb=np.zeros(arr.shape)
w,h,c=arr.shape
for i in range(w):
    for j in range(h):
        _rgb=arr[i][j]
        x=arr[i][j]-rgb
        r,g,b=x
        # if(r*g*b<0):
        # x
        r=max(0,r)
        g=max(0,g)
        b=max(0,b)

        if((b==0 and r==0) or (g==0 and b==0) or (b==0 and g==0)):
            tb[i][j]=[0,0,0]
        else:
            tb[i][j]=x

        # for c in range(3):
        #     x=arr[i][j][c]-rgb[c]
        #     x=max(0,x)
        #     if x==0:
        #         x=255
        #     tb[i][j][c]=x
            # if(arr[i][j][c]<rgb[c]):
            #     # print("?")
            #     tb[i][j][c]=
        # if([i][j][0]<r):
        # print(r,g,b)
# import matplotlib.pyplot as plt
# plt.imshow(tb)
# plt.show()
# import cv2
# cv2.imwrite("test.png",tb)
# arr.mean()
arr=Image.fromarray(np.uint8(tb))
arr.save("test34.png")
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# Img.save("test1.png")
#
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 10
#
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # 图片二值化
# photo = Img.point(table, '1')
# photo.save("test2.png")