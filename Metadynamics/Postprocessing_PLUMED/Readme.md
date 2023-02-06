
#Execute PLUMED

plumed driver --plumed z_cn_xy.txt --mc massnoh.txt --mf_dcd m2d-prot-lig-noh.dcd

#z_cn_xy.txt is the master file. metanoh.pdb and massnoh.txt are structural input files. m2d-protein-lig-noh.dcd is the metadynamics trajectory.


#Reconstruct PMF from biased reaction coordinates (ie, z-position and protein--ligand number of coordinations) 

plumed sum_hills --min -10,0 --max 25,300 --bin 35,30 --hills dzhills --mintozero --sigma 0.5,5 --kt 2.57 --outfile plumedpmf.dat 

#Unit in PLUMED is kj/mol. One would need to convert to kcal/mol.

#Calculate the real dissociation time. Use after executing PLUMED.

python cal_realexittime.py
