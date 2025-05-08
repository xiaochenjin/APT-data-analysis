import numpy as np
from operator import itemgetter

with open ("../../GeSn-raw-data.txt") as f1:
	atom_species_list = np.loadtxt(f1, delimiter=' ', usecols=(0),dtype = 'str',unpack=True)

with open ("../../GeSn-raw-data.txt") as f1:
	atom_position_x_list,atom_position_y_list,atom_position_z_list = np.loadtxt(f1, delimiter=' ', usecols=(1,2,3),unpack=True)


#Don't forget to convert from nm to Ang
atom_position_x_list = [10*value for value in atom_position_x_list]
atom_position_y_list = [10*value for value in atom_position_y_list]
atom_position_z_list = [10*value for value in atom_position_z_list]
atom_position_list = list(zip(atom_species_list,atom_position_x_list,atom_position_y_list,atom_position_z_list))

#chosen_ratio = 0.5
#xlo,xhi = chosen_ratio*min(atom_position_x_list),chosen_ratio*max(atom_position_x_list)
#ylo,yhi = chosen_ratio*min(atom_position_y_list),chosen_ratio*max(atom_position_y_list)
#zlo,zhi = (1-chosen_ratio)*max(atom_position_z_list),max(atom_position_z_list)

xlo,xhi = -200,200
ylo,yhi = -200,200
zlo,zhi = 2000,5000

atom_position_list_box = []			 
for atom_position in atom_position_list:
	if xlo <= atom_position[1] <= xhi and ylo <= atom_position[2] <= yhi and zlo <= atom_position[3] <= zhi:
		atom_position_list_box.append(atom_position)

print("Number of atoms in the box: ", len(atom_position_list_box))

#write into xyz format:
#cell matrix: see 20190701 slides
a = [xhi-xlo,0,0]
b = [0,yhi-ylo,0]
c = [0,0,zhi-zlo]

file_name = 'large-cube-GeSn-raw-APT.xyz'
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
