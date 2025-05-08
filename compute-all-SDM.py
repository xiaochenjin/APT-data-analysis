import numpy as np
import random
import pure_SDM_2
import read_xyz
from optparse import OptionParser

#GET ARGUMENTS
parser = OptionParser()
parser.add_option('--dimension', type = int,default = 10,help = 'unit is nm (default: %default)')
parser.add_option('--direction', type = str,default = 'z',help = 'direction of SDM (default: %default)')
parser.add_option('--PBC', type = str,default = 'True',help = 'whether to use PBC (default: %default)')

(options, args) = parser.parse_args()
dimension = options.dimension #nm
direction = options.direction
PBC = options.PBC

#basic structure info
#species = ['Ge']

input_name = '{0}x{0}x{0}-cube-GeSn-raw-APT.xyz'.format(str(dimension))
#input_name = 'denser-cube-Ge-raw-APT.xyz'
frac_position_list,cell_geometry = read_xyz.read(input_name)
#print(cell_geometry)


N_bin = int(1000*dimension)
D_list,SDM_list = pure_SDM_2.SDM(frac_position_list,cell_geometry,N_bin,direction,PBC)

output_name = direction+'-'+'SDM-{0}x{0}x{0}-cube-GeSn.txt'.format(str(dimension))
#output_name = 'rdf-denser-cube-Ge.txt'
with open (output_name,"w") as f1:
	for i in range(N_bin):
		f1.write(str(D_list[i])+' '+str(SDM_list[i])+'\n')
f1.close()




