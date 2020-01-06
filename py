import matplotlib       
import matplotlib.pyplot as plt
import numpy as np
##############################################
from mpl_toolkits.mplot3d.axes3d import Axes 3D
#################################################
alpha = 0.7
z = 2 * np.pi * 0.5
##################################################
def surface_potential(x,y):
  return 2 + n - 2 * np.cos(x) * np.cos(y) - alpha * np.cos(z - 2 * x)
#defining x and y as independent numpy arrays
x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
#defining 2-dimensional numpy array function
X,Y = np.meshgrid(x, y)
Z = surface_potential(X, Y).T
######################################################
matplotlib.rcParams.update({'font.size':12, 'font.family': 'sans'
######################################################
fig = plt.figure(figsize=(40,15))
ax = fig.add_subplot(1,1,1, projection = '3d')
q = ax.plot_surface(X,Y,Z, rstride=5, cstride=5, cmap=matplotlib.cm.coolwarm, linewidth = 0, antialiased = True)
cb = fig.colorbar(q, shrink=1)
