

for i in $(seq 65 1 336)
do
	~/bin/namd2 res-$i.namd > res-$i.log
	awk '/^ENERGY:/' res-$i.log | awk '{print $2,$7,$8,$12}' > res-$i.dat 

done
