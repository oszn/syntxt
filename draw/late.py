import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=False) #使用latex
# plt.rc('text.latex',unicode=True)
plt.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
plt.rc('text.latex',preamble=r'\usepackage[utf8]{babel}')


def fig2data(fig):
    """
    fig = plt.figure()
    image = fig2data(fig)
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    import PIL.Image as Image
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    # image = np.asarray(image)
    image.save("./1.png")
    return image


figure = plt.figure()
plot = figure.add_subplot(111)
from PIL import Image
img=Image.open("./2.png")
# x = np.linspace(-3,3,100)
# y = np.sin(x)
plot.imshow(img)


# plt.plot(x,y,'r')
# plt.xlabel(r'x') #一定要加r转义，避免将$读错
# plt.ylabel(r'y')
plot.text(100,100,r'$\Omega=\theta+\delta+\phi$',) #在位置(-1.5,0.5)处开始写公式
# plt.show()

fig2data(figure)