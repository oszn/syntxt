from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# x=random.normal


x=random.normal(loc=1,scale=0.001,size=100)
sns.distplot(x, hist=False)
plt.show()