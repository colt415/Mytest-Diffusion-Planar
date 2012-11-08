#Generate initial 2D grid
from netCDF4 import Dataset
import numpy as np
from numpy import *

grid=Dataset('diffusion_planar.nc','w')

grid.createDimension('x',64)
grid.createDimension('y',64)

grid.createVariable('nx','i4',())
grid.createVariable('ny','i4',())

dx=grid.createVariable('dx','f4',('x','y',))
dy=grid.createVariable('dy','f4',('x','y',))

T=grid.createVariable('temperature','f4',('x','y',))

grid.variables['nx'][:]=64
grid.variables['ny'][:]=64

dx[:,:]=0.05
dy[:,:]=0.05

T[:,:]=0.0

grid.close()






