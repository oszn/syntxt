from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random
import pygame
import os
import shutil
from seg import picInput,img_data
word_color = [(142, 143, 142), (126, 135, 255), (0, 0, 0), (191, 69, 0), (255, 0, 0)]
#灰  蓝 黑 暗红 红
import cv2
class txt():

    def __init__(self):
        self.set_font()
        self.set_color()
        self.box=[]
        self.init_color_font()
    def set_img(self, img):
        self.buff=np.zeros(img.size[0:2])
        self.width,self.height=img.size[0:2]
    def set_font(self, path="../font/simsun.ttc", size=36):
        font = ImageFont.truetype(path, size)
        self.font = font
        # print(size)
        return font

    def set_color(self, fill=(0, 0, 0)):
        self.fill = fill
        return fill
    def get_point(self,point,char_size):
        # pass
        '''
        :param ponit:
        :param chat_size:
        :return:
        a1-----a2
        1       1
        1       1
        a3-----a4
        '''
        x, y = point
        w, h = char_size
        x1 = x + w
        y1 = y + h
        a1 = [x, y]
        a2 = [x1, y]
        a3 = [x, y1]
        a4 = [x1, y1]
        return [a1, a2, a4, a3]
    def if_cross(self,ponit,chat_size):



        width,height=self.buff.shape
        x,y=ponit
        w,h=chat_size
        x1=x+w
        y1=y+h
        if x1>width or y1>height:
            return False
        s = self.buff[x:x1, y:y1].sum()
        if(s!=0):
            return False
        self.buff[x:x1,y:y1]=1
        return True
    def init_color_font(self):
        self.color_rd,self.color_slice=get_color()
        self.font_size,self.font_slice,self.font_start=get_font_size()

    def get_color_rand(self):

        _color=random.randint(0,self.color_slice)
        # if if_color:
        _color=int(_color)%len(self.color_rd)
        now_color=word_color[int(self.color_rd[_color])]
        fill=now_color

        self.set_color(fill)
    def get_font_size(self):
        _font_size=random.randint(0,self.font_slice)
        _font_size = int(_font_size)
        _font_size=self.font_size[_font_size%len(self.font_size)]+self.font_start
        _font_size=int(_font_size)
        self.set_font(size=_font_size)

    def draw_txt(self, img, point, content, if_numpy=True):
        draw = ImageDraw.Draw(img)
        # self.set_img(img)
        width,height=img.size[0:2]
        step=10

        self.get_font_size()
        self.get_color_rand()
        char_size = self.font.getsize(content)
        while not self.if_cross(point,char_size) and step:
            step-=1
            point[0]=random.randint(0,width-char_size[0])
            point[1]=random.randint(0,height-char_size[1])
            # print(step)
        assert (step!=0)
        draw.text(point, content, font=self.font, fill=self.fill)
        if if_numpy:
            img = np.array(img)
        return img,self.get_point(point,char_size)

class cv2txt(txt):
    def __init__(self):
        super().__init__()

    def set_font(self, path="../font/msyhl.ttc", size=36):
        font = ImageFont.truetype(path, size)
        self.font = font
        # print(size)
        self.path=path
        return font
    # def add_txt(self):
    #     pass
    # def prefix
    def draw_txt(self, img, point, content, if_numpy=True):
        width = self.width
        height=self.height
        step = 10

        self.get_font_size()
        self.get_color_rand()
        # char_size = self.font.getsize(content)
        char_size,_=cv2.getTextSize(content, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, thickness=5)
        while not self.if_cross(point, char_size) and step:
            step -= 1
            point[0] = random.randint(0, width - char_size[0])
            point[1] = random.randint(0, height - char_size[1])
            # print(step)
        assert (step != 0)
        img=np.array(img)
        point=tuple(point)
        cv2.putText(img, content,point, cv2.FONT_HERSHEY_COMPLEX, 2.0, self.fill, 5)
        # draw.text(point, content, font=self.font, fill=self.fill)
        if if_numpy:
            img = np.array(img)
        return img, self.get_point(point, char_size)
        pass
import math
class pygametxt(txt):
    def __init__(self):
        pygame.init()
        super().__init__()

    def get_point(self, point, char_size,angle,text_create):
        x,y=point
        if angle==0:
            return super().get_point(point,char_size)
        # pass
        w,h=char_size
        center=text_create.get_rect().center
        box=[]
        box.append(self.rec_rorate(w, h, angle))
        box.append(self.rec_rorate(w, -h, angle))
        box.append(self.rec_rorate(w, h, 180 + angle))
        box.append(self.rec_rorate(w, -h, 180 + angle))
        for i in range(4):
            box[i][0] += center[0] + point[0]
            box[i][1] += center[1] + point[1]
            box[i] = tuple(box[i])
        box=tuple(box)
        return box

    def if_cross(self,ponit,chat_size,angle,text_create):
        if angle==0:
            return super(pygametxt, self).if_cross(ponit,chat_size)
        width,height=self.buff.shape
        x,y=ponit
        w,h=chat_size
        tmp=self.rotate(text_create,angle)
        _,_,tmpx,tmpy=tmp.get_rect()
        center=tmp.get_rect().center
        cx,cy=tmp.get_size()

        if tmpx+x>width or tmpy+y>height:
            return False
        cx+=x
        cy+=y

        s=self.buff[x:cx,y:cy].sum()

        if(s!=0):
            return False
        self.buff[x:cx,y:cy]=1
        return True


    def rotate(self,txt_render,angle):
        text=pygame.transform.rotate(txt_render,angle)
        return text
    def set_font(self, path="../font/simsun.ttc", size=36):
        fontObject = pygame.font.Font(path, size)
        self.font = fontObject
        # print(size)
        self.font.set_bold(True)
        return fontObject
    def set_rorate_angle(self):
        n=random.randint(0,9)
        angle=0
        if n<=1:
            angle=random.randint(-80,80)
            # print(angle)
        # for i in range(100):
        return angle
        #     print(random.randint(0,10))
    def rec_rorate(self,w,h,angle):
        w = w // 2
        h = h // 2
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(-angle) for p in box]
        # print(box_rotate)
        return [int(box_rotate[2].x), int(box_rotate[2].y)]
    def draw_txt(self, img, point, content, if_numpy=True):
        width=self.width
        height = self.height
        step = 10

        self.get_font_size()
        self.get_color_rand()
        creat_txt = self.font.render(content, True, self.fill)
        # creat_txt = self.rotate(creat_txt, -30)

        # char_size = self.font.getsize(creat_txt)
        x,y,ztw1,zth1=creat_txt.get_rect()
        char_size=ztw1,zth1
        angle=self.set_rorate_angle()
        # tmp=self.rotate(creat_txt,angle)
        # center=tmp.get_rect().center
        while not self.if_cross(point, char_size,angle,creat_txt) and step:
            step -= 1
            point[0] = random.randint(0, width - char_size[0])
            point[1] = random.randint(0, height - char_size[1])
            angle=self.set_rorate_angle()
            # tmp=self.rotate(creat_txt,angle)
            # print(f"step:{step} angle:{angle}")
        assert (step != 0)
        point=tuple(point)
        # print(f"angle:{angle}")
        creat_txt=self.rotate(creat_txt,angle)
        img.blit(creat_txt,point)
        # draw.text(point, content, font=self.font, fill=self.fill)
        if if_numpy:
            img = np.array(img)
        return img, self.get_point(point, char_size,angle,creat_txt)
def rand_it(radio=0.7):
    a = random.uniform(0, 1)
    return a < radio


def get_dict():
    d = []
    with open("../dict/chinese_cht_dict.txt",encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            d.append(line)
    return d, len(d)


def get_normal(arrlen):
    sampleNo = 1000
    mu = 85
    sigma = 4
    np.random.seed(0)
    s = np.random.normal(mu, sigma, sampleNo)
    # s=s/s.sum()
    output=[]
    _sum=s.sum()
    _new_sum=0
    slice=int(sampleNo/arrlen)
    for i in range(arrlen):
        _sl=min((i+1)*slice,sampleNo)
        # print(_sl)
        tmp=s[i*slice:_sl].sum()
        output.append(tmp/_sum)
        _new_sum+=tmp
    # print(_sum,_new_sum)
    return output

def get_similir_normal(arrlen):
    sampleNo = 1000
    mu = 0
    sigma = 0.1
    np.random.seed(0)
    s = np.random.normal(mu, sigma, sampleNo)
    # s=s/s.sum()
    output=[]
    _sum=s.sum()
    _new_sum=0
    slice=int(sampleNo/arrlen)
    for i in range(arrlen):
        _sl=min((i+1)*slice,sampleNo)
        # print(_sl)
        tmp=s[i*slice:_sl].sum()
        output.append(tmp/_sum)
        _new_sum+=tmp
    # print(_sum,_new_sum)
    return output

def return_with_radioList(arrlen,radio_list):
    rd = np.zeros(arrlen)
    last = 0
    for i in range(0, len(radio_list), 1):
        s = int(last * arrlen)
        e = int((radio_list[i] + last) * arrlen + last)
        rd[s:e] = i
        last = radio_list[i] + last
    return rd



def get_color():
    slice=100
    radio_list=[0.4,0.1,0.15,0.15,0.1]
    rd=return_with_radioList(slice,radio_list)
    return rd,slice

def get_font_size():
    slice=100
    # radio_list=[]
    start=26
    end=34
    hid=end-start
    radio_list=get_normal(hid)
    # print(radio_list.sum())
    radio_list=return_with_radioList(slice,radio_list)
    # for i in range(start,end,1):
    return radio_list,slice,start

def get_txt(num,start=1, radio=None):
    if radio is None:
        radio = [0.05,0.3, 0.15, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    # ### 取大小
    slice=100
    word_dict,word_len=get_dict()
    rd=return_with_radioList(slice,radio)
    words_list=[]
    for i in range(num):
        a=int(random.uniform(0,1)*slice)
        size=int(rd[a])+start
        out=rand_sample(word_len,size)
        words=""
        for i in out:
            words+=word_dict[i]
        words_list.append(words)
    return words_list

def draw_txt(t,img):
    assert isinstance(t,txt)

    # t = txt()
def get_num(n=4):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    out = rand_sample(len(num), n)
    st = ""
    for i in out:
        st += str(i)
    return st

def get_all_num(n):
    result=[]
    for i in range(n):
        result.append(get_num())
    return result
def rand_sample(len, k):
    return random.sample(range(1, len), k)


def main():
    # pygametxt().set_rorate_angle()
    # print(get_similir_normal(10))
    # return
    # pass
    t=pygametxt()
    ##仅仅生成空图
    only_empty=False

    pic_hub=picInput()
    pic_hub.add_from_path("../empty")
    dx = "tmp"
    for i in range(5):
        rand_words=random.randint(5,10)
        rand_num=random.randint(5,10)
        words=get_txt(rand_words)
        nums=get_all_num(rand_num)
        print(i)
        words=words+nums
        # _w,_h=get_w_h(height,width,row,cow)
        pic=pic_hub.get_one_pic()
        img=pic.crop()

        if not only_empty:
            cow=pic.cow
            row=pic.row
            f=open(f"./labels/{i}.png.txt","w+",encoding="utf8")
            t.set_img(img)

            if not os.path.exists(dx):
                os.mkdir(dx)
            path_tmp=f"./{dx}/{i}.png"
            img.save(path_tmp)
            img=pygame.image.load(path_tmp)
            for word in words:
                point = [random.randint(0, cow), random.randint(0, row)]
                img,po=t.draw_txt(img,point,word,if_numpy=False)
                for _point in po:
                    f.write(f"{_point[0]},{_point[1]},")
                f.write(word)
                f.write("\n")
            f.close()
        # cv2.imshow("1.",img)
        # cv2.waitKey(0)

        pygame.image.save(img,f"./test/{i}.png")
        # img.save(open(f"./test/{i}.png","w+"),'png')
    # dx = "tmp"
    shutil.rmtree(f"./{dx}")
if __name__ == '__main__':
    # img=Image.open("../1.png")
    # t=txt()
    # img=t.draw_txt(img,[100,100],"武汉",if_numpy=False)
    # img.save("./2.png")
    # get_normal(10)

    main()

    # t=txt()
    # draw_txt(t)
    # get_txt(10)
    # print(get_num())

