import numpy as np
from operator import itemgetter

infile =  open("all-raw-data.txt",'r')
data = infile.readlines()
infile.close()

print("Total number of atoms: ", len(data))

atom_position_list_Ge = []
atom_position_x_list_Ge = []
atom_position_y_list_Ge = []
atom_position_z_list_Ge = []

atom_position_list_Sn = []
atom_position_x_list_Sn = []
atom_position_y_list_Sn = []
atom_position_z_list_Sn = []

for line in data:
	atom_position_x = float(line.split()[0])
	atom_position_y = float(line.split()[1])
	atom_position_z = float(line.split()[2])
	atom_position = [atom_position_x,atom_position_y,atom_position_z]
	if "Ge:1" in line:
		atom_position_list_Ge.append(atom_position)
		atom_position_x_list_Ge.append(atom_position_x)
		atom_position_y_list_Ge.append(atom_position_y)
		atom_position_z_list_Ge.append(atom_position_z)
	if "Sn:1" in line:
		atom_position_list_Sn.append(atom_position)
		atom_position_x_list_Sn.append(atom_position_x)
		atom_position_y_list_Sn.append(atom_position_y)
		atom_position_z_list_Sn.append(atom_position_z)

	
print("Number of Ge atoms: ", len(atom_position_list_Ge))
print("Dimension of x (nm): ", min(atom_position_x_list_Ge), max(atom_position_x_list_Ge))
print("Dimension of y (nm): ", min(atom_position_y_list_Ge), max(atom_position_y_list_Ge))
print("Dimension of z (nm): ", min(atom_position_z_list_Ge), max(atom_position_z_list_Ge))

print("Number of Sn atoms: ", len(atom_position_list_Sn))
print("Dimension of x (nm): ", min(atom_position_x_list_Sn), max(atom_position_x_list_Sn))
print("Dimension of y (nm): ", min(atom_position_y_list_Sn), max(atom_position_y_list_Sn))
print("Dimension of z (nm): ", min(atom_position_z_list_Sn), max(atom_position_z_list_Sn))

atom_position_list_Ge = sorted(atom_position_list_Ge, key=itemgetter(2))
atom_position_list_Sn = sorted(atom_position_list_Sn, key=itemgetter(2))

with open ("GeSn-raw-data.txt",'w') as f1:
	for i in range(len(atom_position_list_Ge)):
		atom_position = atom_position_list_Ge[i]
		f1.write('Ge '+str(atom_position[0])+' '+str(atom_position[1])+' '+str(atom_position[2])+'\n')
	for i in range(len(atom_position_list_Sn)):
		atom_position = atom_position_list_Sn[i]
		f1.write('Sn '+str(atom_position[0])+' '+str(atom_position[1])+' '+str(atom_position[2])+'\n')
f1.close()
		
