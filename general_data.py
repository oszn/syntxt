from draw.setPic import *
import file_config as fconfig
import threading
import time
if __name__ == '__main__':

    if not os.path.exists(fconfig.save_path):
        os.mkdir(fconfig.save_path)
    if not os.path.exists(fconfig.label_path):
        os.mkdir(fconfig.label_path)
    if not os.path.exists(fconfig.img_path):
        os.mkdir(fconfig.img_path)

    t=pygametxt()
    main(0,10,t,1)
    sx=fconfig.num_txt+fconfig.num_pytxt
    z=0

    # for i in range(0,fconfig.num_txt):
    #     t=txt()
    #     tmp=threading.Thread(target=main,args=(i*fconfig.base,(i+1)*fconfig.base,t,z,))
    #     # main()
    #     tmp.start()
    # for i in range(fconfig.num_txt,sx,1):
    #     t=pygametxt()
    #     tmp = threading.Thread(target=main, args=(i * fconfig.base, (i + 1) * fconfig.base, t, z,))
    #     tmp.start()
    # while(z):
    #     time.sleep(3)
    #     print(z)