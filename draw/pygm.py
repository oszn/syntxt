#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 下午3:15
# @Author  : Jay.Chen
# @File    : Pygame_fonts.py
# @Software: PyCharm

import pygame
import os
from PIL import Image,ImageDraw

# 生成图像
image = Image.new('RGB', (512, 224), (255, 255, 255))
# 将图像保存下来
image.save(open(str(1) + '.png', 'wb'), 'png')
# 初始化
pygame.init()
# 读取图像
img = pygame.image.load('2.png')
# 导入字体
fontType = os.path.join("../font/simsun.ttc")
# 设置一个字体对象
fontObject = pygame.font.Font(fontType, 32)
#得到预计输入字体的所需大小
# print(fontObject.size('xs'))
#设置加粗
fontObject.set_bold(True)
#设置斜体
# fontObject.set_italic(True)
#设置下划线
# fontObject.set_underline(True)
#创建文本surface
angle=10
create_text = fontObject.render('我是', True, (0, 0, 0)) #文本、抗锯齿、字体颜色、背景颜色
_, _, ztw1, zth1 = create_text.get_rect()
print(ztw1,zth1)

# box=[pygame.math.Vector2(p) for p in [(0,0),(ztw1,0),(ztw1,-zth1),(0,-zth1)]]
# box_rotate=[p.rotate(angle) for p in box]
# box=[]
# for i in box_rotate:
#     print(i.x,i.y)
#     box.append((int(50+i.x),int(50-i.y)))
    # print(i.x)
    # print(type(i.x))
# print(box_rotate)
def pol(w,h,angle):
    w=w//2
    h=h//2
    box=[pygame.math.Vector2(p) for p in [(0,0),(w,0),(w,-h),(0,-h)]]
    box_rotate=[p.rotate(-angle) for p in box]
    print(box_rotate)
    return [int(box_rotate[2].x),int(box_rotate[2].y)]
# create_text=pygame.transform.rotate(create_text,angle)
# print(zth1,ztw1)
box=[]

box.append(pol(ztw1,zth1,angle))
box.append(pol(ztw1,-zth1,angle))
box.append(pol(ztw1,zth1,180+angle))
box.append(pol(ztw1,-zth1,180+angle))
#surface的复制
ran=[angle]
center=create_text.get_rect().center
rec=create_text.get_size()
print(center)
for i in ran:
    tmp = pygame.transform.rotate(create_text, i)
    img.blit(tmp, (50, 50)) #文本surface、复制到目标surface的起始坐标
    center=tmp.get_rect().center
    # center[0]+=50
    # center[1]+=50
    rec=tmp.get_size()
    for i in range(4):
        box[i][0]+=center[0]+50
        box[i][1]+=center[1]+50
        box[i]=tuple(box[i])
box=tuple(box)
pygame.image.save(img, 'b.png')

print(box)
img=Image.open("b.png")
draw_left = ImageDraw.Draw(img)
draw_left.polygon(box)
# draw_left.point((50,50),fill=(111,100,120))
# draw_left.rectangle((50,50,120,150),fill=None,outline=(255,0,0))
# draw_left.rectangle((0,0,center[0],center[1]),fill=None,outline=(255,0,0))
# draw_left.rectangle((0,0,rec[0],rec[1]),fill=None,outline=(255,0,0))
# draw_left.ellipse(((50, 50), (250, 250)), fill=None, outline=(0, 0, 255), width=5)
import matplotlib.pyplot as plt
import  numpy as np

img=np.array(img)

# img_left = Image.blend(img, draw_left, 0.5)
plt.imshow(img)

plt.show()