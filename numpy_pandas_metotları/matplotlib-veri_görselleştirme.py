import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from markdown_it.rules_core import inline
x=np.arange(1,6)
y=np.arange(2,11,2)
"""
print(plt.plot(x,y,"red"))
plt.show()
"""
plt.subplot(2,2,1)
a=plt.plot(x,y,"red")
print(a)
plt.subplot(2,2,2)
b=plt.plot(x,y,"blue")
print(b)
plt.subplot(2,2,3)
c=plt.plot(x,y,"green")
print(c)
plt.subplot(2,2,4)
d=plt.plot(x,y,"yellow")
print(d)
plt.show()