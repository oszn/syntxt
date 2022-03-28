# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
import os
import random
from util._random import probabilityRandom

proRandom=probabilityRandom()

class img_data():
    def __init__(self,path,size=(1280,720)):
        self.cow=size[0]
        self.row=size[1]
        self.path=path
        self.get_origin_wid()

    def get_origin_wid(self):
        img,height,width=get_origin_pic(self.path)
        self.img=img
        self.height=height
        self.width=width
    def get_w_h(self):
        return get_w_h(self.height,self.width,self.row,self.cow)

    def crop(self):
        _h,_w=self.get_w_h()
        p400=proRandom.get_out_arr("norm",400)
        p600=proRandom.get_out_arr("norm",600)
        row=random.choice(p400)+500
        cow=random.choice(p600)+700
        # cow,row=self.get_cow_row()

        img=self._crop(self.img,_h,_w,cow,row)
        return img

    def _crop(self,img,hei,wid,cow,row):

        _w=min(self.width-1,wid+cow)
        _h=min(self.height-1,hei+row)
        # print(self.height,self.width,cow, row,wid,hei,_h,_w,"????????")
        img=img.crop((wid,hei,_w,_h))
        return img

def get_empty(path):
    dirs=os.listdir(path)
    empty_list=[]
    for i in dirs:
        d=os.path.join(path,i)
        img_process=img_data(d)
        empty_list.append(img_process)
    return empty_list
## 出口
class picInput():
    def __init__(self):
        self.pic_list=[]
        pass

    def add_pic(self,pic):
        assert isinstance(pic,img_data)
        self.pic_list.append(pic)

    def add_from_path(self,path):
        ep_list=get_empty(path)
        self.add_from_list(ep_list)

    def get_rand(self):
        l= len(self.pic_list)
        return random.randint(0,l-1)

    def add_from_list(self,_list):
        assert isinstance(_list,list)
        for i in _list:
            assert isinstance(i,img_data)
        self.pic_list+=_list
    def get_one_pic(self):
        r=self.get_rand()
        # print(r)
        pic=self.pic_list[r]
        return pic

def main():
    path="./data/hhht2.png"
    cow=1280
    row=720
    img = Image.open(path)
    height, width = img.size
    _h=rand_get(height-row)
    _w=rand_get(width-cow)
    # _img=crop(img,_h,_w,cow,row)
    # save(_img,"1.png")
# def rand_get_img(img,h,w,cow,row):
def save(img,path):
    img.save(path)
def get_origin_pic(path):
    # path = "../data/hhht2.png"
    # cow = 1280
    # row = 720
    img = Image.open(path)
    width, height = img.size
    return img,height,width
def get_w_h(height,width,row,cow):
    _h = rand_get(height - row)
    _w = rand_get(width - cow)
    # print(_h,_w,height,width,row,cow,"fffff")
    return _h,_w

def rand_get(val):
    h=random.randint(0,val)
    return h
    # c=random.randint(0,width)
def read(path,output):
    if not os.path.exists(output):
        os.mkdir(output)
    cow=1280
    row=720
    img=Image.open(path)
    height,width=img.size
    cow_step=int(height/cow)
    row_step=int(width/row)
    for i in range(cow_step):
        for j in range(row_step):
            new_img=img.crop((i*cow,j*row,(i+1)*cow,(j+1)*row))
            new_img.save(f"./{output}/{i}_{j}.png")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name="FIN96"
    path=f"./data/{name}.png"
    main()
    # read(path,name)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
