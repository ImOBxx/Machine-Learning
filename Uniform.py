import numpy as np 
from numpy import random
import matplotlib.pyplot as plt


x = np.random.uniform(0.0, 5.0, 250)

print(x)

plt.hist(x, 5)

plt.show()

x1 = random.normal(0.0, 5.0, 1000000)


print(len(x1))

plt.hist(x, 100)

plt.show()