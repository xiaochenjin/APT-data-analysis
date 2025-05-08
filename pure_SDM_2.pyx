cimport numpy as np
import numpy as np
from libc.math cimport sqrt

cpdef tuple SDM(list atom_position_list,list cell_geometry,int N_bin, str direction,str PBC):
	cdef int N_total 
	N_total = len(atom_position_list)
	cdef list a,b,c,SDM_list=[],M,D_list=[],Dij_list=[],atom_i,atom_j
	a = cell_geometry[0];b = cell_geometry[1];c = cell_geometry[2]

	cdef float V,density_0,dr,rij
	cdef np.ndarray H, H_T,s_vector,r_vector

	V = np.dot(a,np.cross(b,c))
	H_T = np.array([a,b,c])
	H = H_T.transpose() #CELL MATRIX
	density_0=N_total/V

	cdef float lx,ly,lz
	lx = np.linalg.norm(a)
	ly = np.linalg.norm(b)
	lz = np.linalg.norm(c)
	if direction == 'x': d = (0.5*lx)/N_bin
	if direction == 'y': d = (0.5*ly)/N_bin
	if direction == 'z': d = (0.5*lz)/N_bin
	if direction == 'xy': d = (0.5*min(lx,ly))/N_bin

	for n in range(N_bin):
		D = d*(n+1)
		D_list.append(D)

	M=[0]*N_bin #list of m
	for i in range(N_total):
		atom_i = atom_position_list[i]	
		for j in range(i+1,N_total):
			atom_j = atom_position_list[j]
			s_xij = atom_j[0] - atom_i[0]
			s_yij = atom_j[1] - atom_i[1]	
			s_zij = atom_j[2] - atom_i[2]
			if PBC == 'True':
				s_xij=s_xij-round(s_xij)
				s_yij=s_yij-round(s_yij)
				s_zij=s_zij-round(s_zij)
			s_vector=np.array([s_xij,s_yij,s_zij])
			s_vector=np.array([s_xij,s_yij,s_zij])
			r_vector=np.matmul(H,s_vector) #CONVERT VECTOR IN CELL VECTOR DIRECTION TO CARTESIAN
#			rij = sqrt(r_vector[0]*r_vector[0]+r_vector[1]*r_vector[1]+r_vector[2]*r_vector[2])
#			k=int((rij-dr)/dr)
#		   if (k<N_bin):
#			   M[k]=M[k]+2
#			if direction == 'x':dij = lx*s_xij
#			if direction == 'y':dij = ly*s_yij
#			if direction == 'z':dij = lz*s_zij
			if direction == 'x': dij = abs(r_vector[0])
			if direction == 'y': dij = abs(r_vector[1])
			if direction == 'z': dij = abs(r_vector[2])
			if direction == 'xy': dij = sqrt(r_vector[0]*r_vector[0]+r_vector[1]*r_vector[1])
#			Dij_list.append(dij)			
#			Dij_list.append(-dij)
			k=int((abs(dij)-d)/d)
			if (k<N_bin):
				M[k] = M[k] + 2	

	#https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
#	counts,bin_edges = np.histogram(Dij_list,bins=N_bin,density=False)

#	for n in range(N_bin):
#		bin_edge = bin_edges[n]
#		D = (bin_edges[n]+bin_edges[n+1])/2
#		D_list.append(D)

	for l in range(N_bin):
		if direction == 'x': dV = 2*ly*lz*d
		if direction == 'y': dV = 2*lx*lz*d
		if direction == 'z': dV = 2*lx*ly*d
		if direction == 'xy':
			dV = 3.14*((D_list[l]+d)**2-D_list[l]**2)*lz
#	   density_dij=(counts[l]/N_total)/dV
		density_dij=(M[l]/N_total)/dV
		SDM=density_dij/density_0
		SDM_list.append(SDM)

	return D_list,SDM_list

