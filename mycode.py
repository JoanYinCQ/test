#%% import packages
import numpy as np
import matplotlib.pyplot as plt
#%% data
x=np.linspace(1,10,num=100)
print('x=',x[0:5])
y=np.sin(x)
print('y=',y[0:5])
#%% plot
plt.plot(x,y)

