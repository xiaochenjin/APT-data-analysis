import os
import numpy as np
from operator import itemgetter
from multiprocessing import Pool

def multiple_cubes(z_index):
	zlo,zhi = z_index*cell_dimension, (z_index+1)*cell_dimension
	for xy_index in range(len(xy_domain_list)):
		xy_domain = xy_domain_list[xy_index]
		x_range,y_range = xy_domain[0],xy_domain[1]
		xlo,xhi = x_range[0],x_range[1]
		ylo,yhi = y_range[0],y_range[1]
		atom_position_list_box = []
		for atom_position in atom_position_list:
			if xlo <= atom_position[1] < xhi and ylo <= atom_position[2] < yhi and zlo <= atom_position[3] < zhi:
				atom_position_list_box.append(atom_position)

		a = [xhi-xlo,0,0]
		b = [0,yhi-ylo,0]
		c = [0,0,zhi-zlo]
		folder_name = "z-index-{0}".format(z_index)
		if not os.path.exists(folder_name):
			os.mkdir(folder_name)
		file_name = os.path.join(folder_name,"cube-index-{0}.xyz".format(xy_index))
		with open (file_name,"w") as f1:
			f1.write(str(len(atom_position_list_box))+'\n')
			f1.write(str(a[0])+' '+str(a[1])+' '+str(a[2])+' '+str(b[0])+' '+str(b[1])+' '+str(b[2])+' '+str(c[0])+' '+str(c[1])+' '+str(c[2])+'\n')
			for atom_position in atom_position_list_box:
				atom_species = atom_position[0]
				atom_position_write1 = float(atom_position[1]) - xlo
				atom_position_write2 = float(atom_position[2]) - ylo
				atom_position_write3 = float(atom_position[3]) - zlo
				f1.write(atom_species+' '+str(atom_position_write1)+' '+str(atom_position_write2)+' '+str(atom_position_write3)+'\n')
		f1.close()


with open ("large-cube-GeSn-raw-APT.xyz") as f1:
	atom_species_list = np.loadtxt(f1, delimiter=' ', usecols=(0),dtype = 'str',unpack=True,skiprows = 2)

with open ("large-cube-GeSn-raw-APT.xyz") as f1:
	atom_position_x_list,atom_position_y_list,atom_position_z_list = np.loadtxt(f1, delimiter=' ', usecols=(1,2,3),unpack=True,skiprows = 2)

atom_position_list = list(zip(atom_species_list,atom_position_x_list,atom_position_y_list,atom_position_z_list))

#chosen_ratio = 0.5
#xlo,xhi = chosen_ratio*min(atom_position_x_list),chosen_ratio*max(atom_position_x_list)
#ylo,yhi = chosen_ratio*min(atom_position_y_list),chosen_ratio*max(atom_position_y_list)
#zlo,zhi = (1-chosen_ratio)*max(atom_position_z_list),max(atom_position_z_list)

#ANGSTROM
Lx = 400
Ly = 400
Lz = 3000

cell_dimension = 100 #Angstrom
#Nz = int(Lz/cell_dimension) #number of division in z direction
Nz = 30

#obtain divisions in xy direction
xy_domain_list = []
Nx = 4
Ny = 4
for i in range(Nx):
	middle_x = Lx/Nx*(2*i+1)/2
	xlo = -0.5*cell_dimension+middle_x
	xhi = 0.5*cell_dimension+middle_x
	x_range = [xlo,xhi]
	for j in range(Ny):
		middle_y = Ly/Ny*(2*j+1)/2
		ylo = -0.5*cell_dimension+middle_y
		yhi = 0.5*cell_dimension+middle_y
		y_range = [ylo,yhi]
		xy_domain = [x_range,y_range]
		xy_domain_list.append(xy_domain)

N_thread = 2
#index = ['005891']#test
if __name__ == '__main__':
	with Pool(N_thread) as pool:
		pool.map(multiple_cubes, np.arange(Nz))

