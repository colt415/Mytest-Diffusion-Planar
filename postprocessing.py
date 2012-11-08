#postprocessing for diffusion problem

from boutdata import collect
#from boutdata import *
#from boututils import *

import os
import subprocess

import matplotlib.pyplot as plt
from matplotlib import *
from matplotlib.backends.backend_pdf import PdfPages

import numpy as np
from numpy import *

T=collect('temperature', path="/home/colt/Research/BOUT/examples/Mytest-diffusion2D-Planar/data")

#print T.shape

#showdata(T[:,:,:,1])

#subprocess.Popen('rm *.png',shell=True)

x=np.arange(0,3.2,0.05)
y=np.arange(0,3.2,0.05)
[X,Y]=meshgrid(x,y)

t=np.arange(0,1.01,0.01)


plt.figure()

theory=1.0+exp(-5*pi**2*t/3.2**2)
plt.subplot(2,2,1)
plt.plot(t,T[:,0,0,0],'ro',t,theory,'b',linewidth=1.5)
plt.title(r'x0=0, y0=0',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'T(x0,y0,t)',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

theory=1.0+cos(pi/4)*cos(pi)*exp(-5*pi**2*t/3.2**2)
plt.subplot(2,2,2)
plt.plot(t,T[:,15,32,0],'ro',t,theory,'b',linewidth=1.5)
plt.title(r'x0=L/4, y0=L/2',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'T(x0,y0,t)',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

theory=1.0+cos(pi/8)*cos(pi/4)*exp(-5*pi**2*t/3.2**2)
plt.subplot(2,2,3)
plt.plot(t,T[:,8,8,0],'ro',t,theory,'b',linewidth=1.5)
plt.title(r'x0=L/8, y0=L/8',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'T(x0,y0,t)',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

theory=1.0-exp(-5*pi**2*t/3.2**2)
plt.subplot(2,2,4)
plt.plot(t,T[:,63,63,0],'ro',t,theory,'b',linewidth=1.5)
plt.title(r'x0=L, y0=L',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'T(x0,y0,t)',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

plt.figure()
CS=plt.contourf(X,Y,T[0,:,:,1].T,20)
plt.title(r'Initial condition $T(x,y,0)=1+cos(\pi x/L) cos(2 \pi y/L)$',fontsize=18)
plt.xlabel(r'x',fontsize=15)
plt.ylabel(r'y',fontsize=15)
CB=plt.colorbar(CS,shrink=0.8,extend='both')
plt.show()


