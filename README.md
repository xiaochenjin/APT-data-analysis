Preliminary codes for APT data analysis

# write_data.py
Convert raw APT data into .txt data file

# write_GeSn_data.py
Output information of specified species

# select-large-box.py
Output data within a specified box (in .xyz format)

# select-multiple-cubes.py
Divide the box into smaller cubes (e.g, 10x10x10 nm3)

# compute-all-pairs.py and all_pair_rdf*
Compute RDF of all the pairs

# compute-all-SDM.py and pure_SDM_2*
Compute SDM of all the pairs

# setup.py
Compile *.pyx into *c and *.so
<br> 
python setup.py build_ext --inplace
