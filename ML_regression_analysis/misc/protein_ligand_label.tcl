
mol load psf finalbound.psf pdb mineq.pdb 

for {set i 65} {$i < 337 } {incr i} {
set all [atomselect top all]
$all set beta 0
set res [atomselect top "protein and resid $i"]
$res set beta 1 
set lig [atomselect top "resname FEN"]
$lig set beta 2
$all writepdb res-${i}.pdb 
}


