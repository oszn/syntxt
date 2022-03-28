# -*- encoding: utf-8 -*-
'''
@File    :   _random.py
@Contact :   1091756452@qq.com
@License :   (C)Copyright 2022-2024
 
@Desciption: 重构代码的关键问题是感觉，这份代码里的随机用到的很多，但是并没有统一起来，所以需要进行重构代码。
这份代码中用到的随机有，文字内容，文字长度，文字字号，文字颜色，文字位置，底图等等。
其中需要考虑到随机分布问题。颜色随机问题要考虑区别底图颜色问题。
todo: 常规函数的分布，生成对应随机数。

@Author: oszn(y.liu)
@Modify Time    
------------ 
2022/3/26 13:08       
'''

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

class probabilityRandom(object):

    def __init__(self):
        self.func={}
        for i in probabilityFuction.__subclasses__():
            k=i()
            self.func[k.get_name()]=k

    def print_func(self):
        print(self.func.keys())

    def get_out_arr(self,name,slice,**kwargs):
        radio=50
        base_arr=self.function(name,size=slice*radio,**kwargs)

        max_nums=base_arr.max()
        pice_slice=max_nums/slice


        for i in range(slice):
            base_arr=np.where((base_arr<pice_slice*(i+1))
                              &(base_arr>pice_slice*i),
                              i,base_arr)
            # print(base_arr)
        base_arr=base_arr.astype(np.int)

        return base_arr


    def function(self,name,**kwargs):
        assert name in self.func.keys(),"no such function,using print_func"
        v=self.func[name]
        out_arr=v.function(**kwargs)
        out_arr=np.array(out_arr)
        out_arr=out_arr-out_arr.min()
        # print(out_arr.shape)
        return out_arr



class probabilityFuction():
    '''
    @keyword
    为毛不能根据基类生成寻找到派生类啊，fw啊
    '''
    def __init__(self):
        pass

    def get_name(self):
        pass

    def function(self):
        pass


class probabilityNormal(probabilityFuction):
    def __init__(self):
        pass

    def function(self,mean=0, var=0.1,size=3000):
        sigma = np.sqrt(var)
        out=norm.rvs(mean,var,size=size)
        out=sorted(out)
        return out

    def get_name(self):
        return "norm"
# normal(0, 0.1)
if __name__ == '__main__':
    # p=probabilityFuction()
    # a=10
    c=probabilityRandom()
    c.print_func()
    c.get_out_arr("norm",20)