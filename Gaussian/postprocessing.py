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

T=collect('temperature', path="/home/colt/Research/BOUT/examples/Mytest-diffusion2D/data")

#print T.shape

#showdata(T[:,:,:,1])

#subprocess.Popen('rm *.png',shell=True)
x=np.arange(0,3.2,0.05)
y=np.arange(0,3.2,0.05)

[X,Y]=meshgrid(x,y)

pp=PdfPages('Diffusion_Gaussian.pdf')

for i in range(101):
  number=str(i+1).zfill(3)
  plt.figure()
  CS=plt.contourf(X,Y,T[i,:,:,0],20)
  CB=plt.colorbar(CS,shrink=0.8,extend='both')
  plt.title(r'Diffusion with Gaussian initial condition, $A=0.5,\sigma=0.64$  '+number,fontsize=15)
  plt.savefig(pp,format='pdf')

pp.close()
  
#plt.figure()
#x=np.arange(0,64,1)
#plt.plot(x,T[0,:,31,0],linewidth=1.5)
#plt.grid(True)
#plt.show()

#print T[0,31,31,1]
