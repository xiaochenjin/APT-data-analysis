import numpy as np

def read(file_name):
	infile = open (file_name,"r")
	data = infile.readlines()
	N_total = int(data[0].split()[0])
#	print(N_total)
#	a = [float(i) for i in data[1].split('"')[1].split()][:3]
#	b = [float(i) for i in data[1].split('"')[1].split()][3:6]
#	c = [float(i) for i in data[1].split('"')[1].split()][6:]
	a = [float(i) for i in data[1].split()[:3]]
	b = [float(i) for i in data[1].split()[3:6]]
	c = [float(i) for i in data[1].split()[6:]]
	cell_geometry = [a,b,c]
	H_T = np.array([a,b,c])
	H = H_T.transpose() #CELL MATRIX
#	print(cell_geometry)
#	print(H)
	frac_position_list = []
	for line in data[2:]:
		atom_species = line.split()[0]
		abs_position = [float(i) for i in line.split()[1:]]
#		print(atom_species,abs_position)
		frac_position = list(np.matmul(np.linalg.inv(H),abs_position))
#		print(frac_position)
		frac_position_list.append(frac_position)

	return frac_position_list, cell_geometry


#file_name = 'GeSn-random-relaxed.xyz'
#read(file_name)
