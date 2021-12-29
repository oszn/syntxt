import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

sampleNo = 10000;
mu = 1
sigma = 0.1
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo)
plt.hist(s,300)
plt.show()